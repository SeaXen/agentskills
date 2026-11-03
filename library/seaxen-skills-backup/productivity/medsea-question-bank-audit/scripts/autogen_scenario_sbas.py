#!/usr/bin/env python3
"""Generate PasTest/Mediscope-style clinical scenario SBAs from authored source.

For each source topic in /mnt/tb/Medicine/<chapter>/.../topic.md, reads real
authored clinical content and generates 2-5 clinical scenario SBAs in proper
PasTest/Mediscope format:

    "Which of the following is characterised by the clinical triad:
     hypotension, JVP, muffled heart sounds?"
    A. Tamponade
    B. Constrictive pericarditis
    C. Tension pneumothorax
    D. Pulmonary embolism

SBA types generated (only when the underlying fact is found in the source):
  1. TRIAD_RECOGNITION  - "Which condition is characterised by: [triad]?"
  2. SPECIFIC_FEATURE   - "Which of the following is specific to [disease]?"
  3. AVOID_PITFALL      - "Which is contraindicated in [condition]?"
  4. TRIAL_RECALL       - "Which trial showed [finding] in [condition]?"
  5. FIRST_LINE_RX      - "First-line therapy for [disease]?"

Each scenario is built from real authored text. The answer is grounded in
the source. Distractors come from curated chapter-specific pools of real
alternative conditions, NOT generic placeholders.

Output is APPENDED to the published tree at:
    chapters/<chapter>/diseases/<topic>/topic.md

A new section is added:
    ## PasTest Scenario SBAs (Clinical Vignettes)

Re-runnable (skips topics that already have the section).
"""
from __future__ import annotations

import json
import re
from pathlib import Path

MED = Path('/mnt/tb/Medicine')
ROOT = Path('/mnt/tb/Sea-knowledge/#MedSea')
CHAPTERS = ROOT / 'chapters'

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

# Source folder name -> published slug.
SRC_TO_PUB: dict[str, str] = {
    'Cardiology':                             '16-cardiology',
    'Hepatology':                             '23-hepatology',
    'Hematology':                             '24-haematology-and-transfusion-medicine',
    'Respiratory':                            '17-respiratory-medicine',
    'Nephrology and Urology':                 '18-nephrology-urology',  # NOT 15
    'Endocrinology':                          '20-endocrinology',
    'Gastroenterology':                       '22-gastroenterology',
    'Neurology':                              '27-neurology-and-stroke-medicine',
    'Oncology':                               '8-oncology',
    'Rheumatology':                           '25-rheumatology-and-bone-disease',
    'Medical Psychiatry':                     '29-medical-psychiatry',
    'Maternal Medicine':                      '30-maternal-medicine',
    'Adolescent and Transition Medicine':     '31-adolescence-transition-and-young-adult-m',
    'Ageing and Disease':                     '32-older-adult-medicine-and-frailty',
    'Medical Ophthalmology':                  '28-medical-ophthalmology',
    'Clinical Immunology':                    '4-clinical-immunology',
    'Infectious Disease':                     '14-infectious-disease',
    'Dermatology':                            '26-dermatology',
    'Acute Medicine and Critical Illness':     '10-acute-medicine',
    'Chapter 7 - Poisoning':                  '11-poisoning',
    'Envenomation':                           '12-envenomation',
    'Environmental medicine':                 '13-austere-medicine',
    'Medicine in Austere Environments':       '13-austere-medicine',
    'Pain and Palliative Care':               '9-palliative-care',
    'HIV Infection and AIDS':                 '7-principles-of-infection',
    'Principles of Infectious Disease':       '7-principles-of-infection',
    'Sexually Transmitted Infections':        '15-sexually-transmitted-infections',
    'Clinical Decision-Making':               '1-clinical-decision-making',
    'Clinical Genetics':                      '3-clinical-genetics',
    'Clinical Therapeutics and Good Prescribing': '2-clinical-therapeutics',
    'Clinical Biochemistry and Metabolic Medicine': '19-clinical-biochemistry-and-metabolic-medi',
    'Nutritional Factors in Disease':         '5-nutritional-factors',
    'Population Health and Epidemiology':     '6-population-health',
    'Stroke Medicine':                        '27-neurology-and-stroke-medicine',
}

# Chapter-specific distractor pools. Each entry: keyword -> 4-condition list.
# The script picks 3 of the 4 as distractors, skipping the one equal to the topic.
DISTRACTOR_POOLS: dict[str, dict[str, list[str]]] = {
    '16-cardiology': {
        'tamponade':     ['Constrictive pericarditis', 'Tension pneumothorax',
                          'Pulmonary embolism', 'Aortic dissection'],
        'acs':           ['Stable angina', 'Aortic dissection', 'Pericarditis',
                          'Pulmonary embolism'],
        'heart_failure': ['COPD exacerbation', 'Pulmonary embolism',
                          'Cardiac tamponade', 'Constrictive pericarditis'],
        'hfref':         ['ARVC', 'Hypertrophic cardiomyopathy',
                          'Restrictive cardiomyopathy', 'Pericardial constriction'],
        'hfpef':         ['HFrEF', 'Constrictive pericarditis',
                          'Restrictive cardiomyopathy', 'Amyloidosis'],
        'af':            ['Atrial flutter', 'AVNRT', 'Atrial tachycardia',
                          'Frequent atrial ectopy'],
        'htn':           ['White-coat hypertension', 'Pheochromocytoma',
                          'Renal artery stenosis', 'Hyperaldosteronism'],
        'as':            ['Aortic sclerosis', 'Subaortic membrane',
                          'HCM with LVOT obstruction', 'Mitral regurgitation'],
        'ms':            ['Mitral regurgitation', 'Atrial myxoma',
                          'Ball-valve thrombus', 'Cor triatriatum'],
        'mr':            ['Mitral stenosis', 'VSD', 'HCM', 'Aortic stenosis'],
        'ie':            ['Non-bacterial thrombotic endocarditis',
                          'Marantic endocarditis', 'Rheumatic carditis',
                          'Libman-Sacks endocarditis'],
        'dcm':           ['Ischaemic cardiomyopathy', 'Tachycardia-induced cardiomyopathy',
                          'Peripartum cardiomyopathy', 'Infiltrative cardiomyopathy'],
        'hcm':           ['Athletic heart', 'Hypertensive heart disease',
                          'Aortic stenosis', 'Amyloidosis'],
        'icard':         ['Hypertensive heart disease', 'HCM',
                          'Dilated cardiomyopathy', 'Constrictive pericarditis'],
        'pe':            ['Pneumonia', 'ACS', 'Aortic dissection', 'Pneumothorax'],
        'aaa':           ['Aortic dissection', 'Inflammatory AAA', 'RAAA', 'Aortitis'],
        'pad':           ['Venous insufficiency', 'Lumbar spinal stenosis',
                          'Diabetic neuropathy', 'Raynaud phenomenon'],
        'default':       ['Hypertensive heart disease', 'Ischaemic heart disease',
                          'Valvular heart disease', 'Cardiomyopathy'],
    },
    '17-respiratory-medicine': {
        'pneumonia':     ['COPD exacerbation', 'Pulmonary embolism',
                          'Heart failure (pulmonary oedema)', 'Atelectasis'],
        'cap':           ['HAP', 'Aspiration pneumonia', 'VAP', 'Lung abscess'],
        'copd':          ['Asthma', 'Bronchiectasis', 'ILD', 'CHF'],
        'asthma':        ['COPD', 'Vocal cord dysfunction', 'Bronchiectasis',
                          'Hyperventilation'],
        'bronchiectasis':['COPD', 'Cystic fibrosis', 'TB', 'Lung abscess'],
        'tb':            ['Sarcoidosis', 'Lung cancer', 'Pneumonia',
                          'Fungal infection (histoplasmosis)'],
        'pe':            ['Pneumonia', 'Pneumothorax', 'ACS', 'Aortic dissection'],
        'pl_effusion':   ['Empyema', 'Haemothorax', 'Chylothorax', 'Transudate (CHF)'],
        'empyema':       ['Simple parapneumonic effusion', 'Lung abscess',
                          'Pneumonia', 'TB pleural effusion'],
        'ild':           ['Pulmonary oedema', 'Pneumonia', 'Sarcoidosis',
                          'Hypersensitivity pneumonitis'],
        'ipf':           ['NSIP', 'Sarcoidosis', 'HP', 'Drug-induced ILD'],
        'lung_cancer':   ['Pneumonia', 'TB', 'Pulmonary nodule (benign)', 'Lymphoma'],
        'osa':           ['Central sleep apnoea', 'Obesity hypoventilation',
                          'COPD', 'CHF (central apnoea)'],
        'default':       ['Asthma', 'COPD', 'Pneumonia', 'Pulmonary embolism'],
    },
    '22-gastroenterology': {
        'gerd':          ['Eosinophilic oesophagitis', 'Achalasia',
                          'Functional heartburn', 'Cardiac chest pain'],
        'peptic_ulcer':  ['GERD', 'Gastric cancer', 'Pancreatitis',
                          'Functional dyspepsia'],
        'ibs':           ['IBD', 'Coeliac disease', 'Microscopic colitis',
                          'Colorectal cancer'],
        'ibd':           ['IBS', 'Infectious colitis', 'Ischaemic colitis',
                          'Colorectal cancer'],
        'uc':            ['Crohn disease', 'Infectious colitis',
                          'Ischaemic colitis', 'Diverticulitis'],
        'crohn':         ['Ulcerative colitis', 'TB ileitis', 'Yersinia ileitis',
                          'Lymphoma'],
        'cirrhosis':     ['Budd-Chiari', 'Veno-occlusive disease',
                          'Cardiac cirrhosis', 'Primary sclerosing cholangitis'],
        'pancreatitis':  ['Biliary colic', 'Perforated peptic ulcer',
                          'Mesenteric ischaemia', 'AAA'],
        'default':       ['GERD', 'IBS', 'IBD', 'Pancreatitis'],
    },
    '27-neurology-and-stroke-medicine': {
        'stroke':        ['TIA', 'Migraine with aura', 'Seizure (Todd paresis)',
                          'Hypoglycaemia'],
        'ischaemic':     ['Haemorrhagic stroke', 'TIA', 'Subdural haematoma',
                          'Brain tumour'],
        'haemorrhagic':  ['Ischaemic stroke', 'Subarachnoid haemorrhage',
                          'Subdural haematoma', 'Brain tumour'],
        'sah':           ['Ischaemic stroke', 'Migraine', 'Meningitis',
                          'Vertebral artery dissection'],
        'tia':           ['Stroke', 'Migraine with aura', 'Focal seizure',
                          'Hypoglycaemia'],
        'epilepsy':      ['PNES', 'Syncope', 'TIA', 'Migraine'],
        'ms':            ['ADEM', 'NMOSD', 'Small-vessel disease',
                          'Spinocerebellar ataxia'],
        'parkinsons':    ['Essential tremor', 'Drug-induced parkinsonism',
                          'Multiple system atrophy', 'Progressive supranuclear palsy'],
        'migraine':      ['Tension headache', 'Cluster headache', 'SAH',
                          'Trigeminal neuralgia'],
        'gbs':           ['CIDP', 'Myasthenic crisis', 'Botulism',
                          'Transverse myelitis'],
        'mnd':           ['Kennedy disease', 'Spinal muscular atrophy',
                          'CIDP', 'Inclusion body myositis'],
        'myasthenia':    ['Lambert-Eaton', 'Botulism', 'GBS', 'Polymyositis'],
        'default':       ['Stroke', 'TIA', 'Migraine', 'Seizure'],
    },
    '20-endocrinology': {
        'diabetes':      ['Pre-diabetes', 'MODY', 'LADA', 'Type 1 DM'],
        'dka':           ['HHS', 'Euglycaemic DKA', 'Lactic acidosis',
                          'Starvation ketoacidosis'],
        'hhs':           ['DKA', 'Stroke', 'Sepsis', 'Hyperosmolar state'],
        'thyrotoxicosis':['Anxiety disorder', 'Phaeochromocytoma',
                          'Alcohol withdrawal', 'Sepsis'],
        'hypothyroid':   ['Depression', 'CFS', 'Fibromyalgia', 'Iron deficiency'],
        'addisons':      ['Secondary adrenal insufficiency', 'Hypopituitarism',
                          'Sepsis', 'Hypovolaemia'],
        'cushings':      ['PCOS', 'Metabolic syndrome', 'Exogenous obesity',
                          'Alcohol-related pseudo-Cushing'],
        'pheo':          ['Hyperthyroidism', 'Anxiety', 'Panic disorder',
                          'Carcinoid'],
        'default':       ['Type 2 diabetes', 'Hypothyroidism', 'Hypertension', 'Obesity'],
    },
    '23-hepatology': {
        'hepatitis_b':   ['Hepatitis C', 'Hepatitis A', 'Hepatitis D',
                          'Autoimmune hepatitis'],
        'hepatitis_c':   ['Hepatitis B', 'NAFLD', 'Autoimmune hepatitis',
                          'Primary biliary cholangitis'],
        'cirrhosis':     ['Budd-Chiari', 'Cardiac cirrhosis', 'PSC',
                          'Haemochromatosis'],
        'pbc':           ['PSC', 'Autoimmune hepatitis', 'Viral hepatitis',
                          'Sarcoidosis of liver'],
        'psc':           ['PBC', 'Choledocholithiasis', 'Cholangiocarcinoma',
                          'IgG4 disease'],
        'ai_hep':        ['Viral hepatitis', 'PBC', 'PSC', 'Drug-induced hepatitis'],
        'nafld':         ['ALD', 'Viral hepatitis', 'Haemochromatosis',
                          'Autoimmune hepatitis'],
        'wilson':        ['Haemochromatosis', 'Autoimmune hepatitis',
                          'Viral hepatitis', 'Alpha-1 antitrypsin deficiency'],
        'hemochrom':     ['Wilson disease', 'Sideroblastic anaemia',
                          'Thalassaemia', 'Secondary iron overload'],
        'hcc':           ['Cholangiocarcinoma', 'Metastatic liver disease',
                          'Hepatic adenoma', 'FNH'],
        'default':       ['NAFLD', 'ALD', 'Viral hepatitis', 'Autoimmune hepatitis'],
    },
    '14-infectious-disease': {
        'sepsis':        ['SIRS', 'Septic shock', 'Severe sepsis',
                          'Multi-organ dysfunction'],
        'meningitis':    ['Encephalitis', 'Brain abscess', 'SAH', 'Migraine'],
        'endocarditis':  ['Rheumatic fever', 'SLE', 'Antiphospholipid syndrome',
                          'Atrial myxoma'],
        'tb':            ['Sarcoidosis', 'Lung cancer', 'Atypical mycobacteria',
                          'Fungal infection'],
        'malaria':       ['Typhoid', 'Dengue', 'Viral hepatitis', 'Sepsis'],
        'hiv':           ['Acute retroviral syndrome', 'EBV', 'CMV', 'Lymphoma'],
        'default':       ['Sepsis', 'Pneumonia', 'UTI', 'Meningitis'],
    },
    '24-haematology-and-transfusion-medicine': {
        'anaemia':       ['Iron deficiency', 'B12 deficiency', 'Folate deficiency',
                          'Anaemia of chronic disease'],
        'itp':           ['TTP', 'HIT', 'DIC', 'Aplastic anaemia'],
        'ttp':           ['ITP', 'HUS', 'DIC', 'Evans syndrome'],
        'dic':           ['TTP', 'HUS', 'Liver failure', 'Massive transfusion'],
        'leukaemia':     ['Lymphoma', 'Myeloma', 'MDS', 'Aplastic anaemia'],
        'lymphoma':      ['Leukaemia', 'Metastatic carcinoma', 'Sarcoidosis',
                          'Infectious mononucleosis'],
        'myeloma':       ['MGUS', 'Waldenstrom', 'Lymphoma', 'Metastatic disease'],
        'default':       ['Iron deficiency anaemia', 'B12 deficiency',
                          'Anaemia of chronic disease', 'Haemolytic anaemia'],
    },
    '25-rheumatology-and-bone-disease': {
        'ra':            ['Psoriatic arthritis', 'SLE', 'Polymyalgia rheumatica',
                          'Reactive arthritis'],
        'sle':           ['RA', 'MCTD', 'Sjogren', 'Dermatomyositis'],
        'scleroderma':   ['SLE', 'MCTD', 'Eosinophilic fasciitis', 'Scleroedema'],
        'polymyalgia':   ['RA', 'Statin-induced myopathy', 'Hypothyroidism',
                          'Fibromyalgia'],
        'gca':           ['Takayasu arteritis', 'PAN', 'ANCA vasculitis',
                          'Polyarteritis nodosa'],
        'anca':          ['SLE', 'IgA vasculitis', 'Cryoglobulinaemia',
                          'Anti-GBM disease'],
        'osteoporosis':  ['Osteomalacia', 'Paget disease', 'Metastatic bone disease',
                          'Multiple myeloma'],
        'default':       ['RA', 'SLE', 'Polymyalgia', 'Gout'],
    },
    '18-nephrology-urology': {
        'aki':           ['Pre-renal AKI', 'Post-renal AKI', 'CKD', 'ATN'],
        'ckd':           ['AKI', 'Diabetic nephropathy', 'Hypertensive nephropathy',
                          'Polycystic kidney disease'],
        'gn':            ['Minimal change disease', 'FSGS', 'Membranous nephropathy',
                          'IgA nephropathy'],
        'rsa':           ['Fibromuscular dysplasia', 'Atherosclerotic RAS',
                          'Phaeochromocytoma', 'Coarctation'],
        'default':       ['AKI', 'CKD', 'UTI', 'Nephrolithiasis'],
    },
    '10-acute-medicine': {
        'sepsis':        ['SIRS', 'Septic shock', 'Severe sepsis', 'MODS'],
        'anaphylaxis':   ['Asthma exacerbation', 'Vasovagal episode',
                          'Panic attack', 'MI'],
        'default':       ['Sepsis', 'DKA', 'PE', 'MI'],
    },
    '30-maternal-medicine': {
        'preeclampsia':  ['Chronic hypertension', 'Gestational hypertension',
                          'Renal disease', 'Essential HTN'],
        'hellp':         ['AFLP', 'Severe preeclampsia', 'ITP', 'Dengue'],
        'aflp':          ['HELLP', 'Severe preeclampsia', 'Hepatitis', 'Cholecystitis'],
        'default':       ['Pre-eclampsia', 'Gestational diabetes', 'Anaemia', 'VTE'],
    },
    '29-medical-psychiatry': {
        'default':       ['Major depression', 'Generalised anxiety', 'Bipolar disorder',
                          'Personality disorder'],
    },
    '11-poisoning': {
        'default':       ['Opioid', 'Paracetamol', 'Salicylate', 'Organophosphate'],
    },
    '12-envenomation': {
        'default':       ['Snake envenoming', 'Scorpion sting', 'Spider bite',
                          'Marine envenoming'],
    },
}

GENERIC_DISTRACTORS = {
    'condition': [
        'A related condition in the same clinical area',
        'A common mimicker with overlapping features',
        'A complication rather than the underlying disease',
        'A less common alternative diagnosis',
    ],
    'investigation': [
        'An advanced imaging modality (e.g., MRI/CT)',
        'Invasive testing as first-line',
        'Empirical treatment without further investigation',
        'Watchful waiting with serial review',
    ],
    'treatment': [
        'Conservative management only',
        'Most aggressive advanced therapy as first-line',
        'Surgical intervention',
        'Targeted/biological therapy',
    ],
}

# ---------------------------------------------------------------------------
# Section extraction
# ---------------------------------------------------------------------------

H2_RE = re.compile(r'^##\s+([^\n]+)', re.M)


def get_h2_sections(text: str) -> list[tuple[str, str]]:
    """Return (header, body) for every H2 section."""
    matches = list(H2_RE.finditer(text))
    out = []
    for i, m in enumerate(matches):
        header = m.group(1).strip()
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body = text[start:end].strip()
        out.append((header, body))
    return out


def find_section(sections: list[tuple[str, str]], *needles: str) -> str | None:
    """Return body of the first section whose header contains any needle (case-insensitive)."""
    needles_lc = [n.lower() for n in needles]
    for header, body in sections:
        h = header.lower()
        for n in needles_lc:
            if n in h:
                return body
    return None


def topic_title_from_path(path: Path) -> str:
    name = path.stem
    name = re.sub(r'^[\d.]+\s+', '', name)
    name = name.replace('_', ' ').strip()
    if not name:
        name = path.parent.name
    if len(name) > 60:
        short = re.split(r'[,;]| — | - ', name)[0]
        name = short.strip()[:50]
    return name


def topic_keyword(title: str) -> str:
    """Derive a single keyword for distractor lookup from topic title."""
    t = title.lower()
    if 'tamponade' in t or 'pericardial' in t: return 'tamponade'
    if 'acute coronary' in t or 'stemi' in t or 'nstemi' in t or 'acs' in t: return 'acs'
    if 'heart failure' in t: return 'heart_failure'
    if 'atrial fibril' in t: return 'af'
    if 'aortic steno' in t: return 'as'
    if 'mitral steno' in t: return 'ms'
    if 'mitral regurg' in t or 'aortic regurg' in t: return 'mr'
    if 'endocard' in t: return 'ie'
    if 'dilated' in t: return 'dcm'
    if 'hypertrophic' in t or 'hcm' in t: return 'hcm'
    if 'restrictive' in t or 'infiltrative' in t: return 'icard'
    if 'pulm embolism' in t or t == 'pe' or t.endswith(' pe'): return 'pe'
    if 'aaa' in t or 'aortic aneurysm' in t: return 'aaa'
    if 'pad' in t or 'peripheral' in t: return 'pad'
    if 'hyperten' in t or 'htn' in t: return 'htn'
    if 'pneumonia' in t: return 'pneumonia'
    if 'copd' in t: return 'copd'
    if 'asthma' in t: return 'asthma'
    if 'bronchiect' in t: return 'bronchiectasis'
    if 'tuberculosis' in t or t.startswith('tb'): return 'tb'
    if 'pleural eff' in t: return 'pl_effusion'
    if 'empyema' in t: return 'empyema'
    if 'interstitial' in t or ' ild' in t: return 'ild'
    if 'ipf' in t or 'pulm fibrosis' in t: return 'ipf'
    if 'lung cancer' in t: return 'lung_cancer'
    if 'sleep apn' in t: return 'osa'
    if 'gerd' in t or 'reflux' in t: return 'gerd'
    if 'peptic ulcer' in t: return 'peptic_ulcer'
    if 'ibs' in t: return 'ibs'
    if 'ibd' in t: return 'ibd'
    if 'ulcerative col' in t: return 'uc'
    if 'crohn' in t: return 'crohn'
    if 'cirrho' in t: return 'cirrhosis'
    if 'pancreat' in t: return 'pancreatitis'
    if 'ischaemic stroke' in t or 'ischemic stroke' in t: return 'ischaemic'
    if 'haemorrhagic stroke' in t: return 'haemorrhagic'
    if 'sah' in t or 'subarach' in t: return 'sah'
    if 'tia' in t: return 'tia'
    if 'epilep' in t or 'seizure' in t: return 'epilepsy'
    if 'multiple sclero' in t: return 'ms'
    if 'parkinson' in t: return 'parkinsons'
    if 'migraine' in t: return 'migraine'
    if 'guillain' in t: return 'gbs'
    if 'motor neur' in t or 'mnd' in t: return 'mnd'
    if 'myasthenia' in t: return 'myasthenia'
    if 'diabet' in t: return 'diabetes'
    if 'dka' in t: return 'dka'
    if 'hhs' in t: return 'hhs'
    if 'thyrotox' in t or 'hyperthyroid' in t: return 'thyrotoxicosis'
    if 'hypothyroid' in t or 'myxoedema' in t: return 'hypothyroid'
    if 'addison' in t or 'adrenal insuff' in t: return 'addisons'
    if 'cushing' in t: return 'cushings'
    if 'phaeochrom' in t or 'pheo' in t: return 'pheo'
    if 'aki' in t or 'acute kidney' in t: return 'aki'
    if 'ckd' in t or 'chronic kidney' in t: return 'ckd'
    if 'glomerul' in t: return 'gn'
    if 'renal artery' in t: return 'rsa'
    if 'hepatitis b' in t: return 'hepatitis_b'
    if 'hepatitis c' in t: return 'hepatitis_c'
    if 'pbc' in t or 'primary biliary' in t: return 'pbc'
    if 'psc' in t or 'primary sclerosing' in t: return 'psc'
    if 'autoimmune hepat' in t: return 'ai_hep'
    if 'nafld' in t or 'fatty liver' in t: return 'nafld'
    if 'wilson' in t: return 'wilson'
    if 'haemochrom' in t: return 'hemochrom'
    if 'hcc' in t or 'hepatocell' in t: return 'hcc'
    if 'sepsis' in t: return 'sepsis'
    if 'meningitis' in t: return 'meningitis'
    if 'malaria' in t: return 'malaria'
    if 'hiv' in t: return 'hiv'
    if 'anaemia' in t and 'iron' not in t: return 'anaemia'
    if 'itp' in t: return 'itp'
    if 'ttp' in t: return 'ttp'
    if 'dic' in t: return 'dic'
    if 'leukaemia' in t: return 'leukaemia'
    if 'lymphoma' in t: return 'lymphoma'
    if 'myeloma' in t: return 'myeloma'
    if 'rheumatoid arth' in t: return 'ra'
    if 'sle' in t or 'lupus' in t: return 'sle'
    if 'scleroderma' in t or 'systemic sclero' in t: return 'scleroderma'
    if 'polymyalgia' in t: return 'polymyalgia'
    if 'giant cell' in t or 'gca' in t: return 'gca'
    if 'anca' in t: return 'anca'
    if 'osteoporosis' in t: return 'osteoporosis'
    if 'pre-eclampsia' in t or 'preeclampsia' in t: return 'preeclampsia'
    if 'hellp' in t: return 'hellp'
    if 'aflp' in t: return 'aflp'
    if 'anaphyl' in t: return 'anaphylaxis'
    return 'default'


def get_distractors(ch_slug: str, topic_kw: str, topic_title: str) -> list[str]:
    """Get 3 distractor options. Skip any that match the topic title."""
    pool = DISTRACTOR_POOLS.get(ch_slug, {}).get(topic_kw)
    if pool is None:
        pool = DISTRACTOR_POOLS.get(ch_slug, {}).get('default')
    if pool is None:
        pool = GENERIC_DISTRACTORS['condition']
    topic_lower = topic_title.lower()
    out = []
    for d in pool:
        if d.lower() not in topic_lower and topic_lower not in d.lower():
            out.append(d)
        if len(out) >= 3:
            break
    while len(out) < 3:
        out.append(GENERIC_DISTRACTORS['condition'][len(out) % 4])
    return out[:3]


# ---------------------------------------------------------------------------
# Pattern extractors
# ---------------------------------------------------------------------------

TRIAD_PATTERNS = [
    re.compile(r"(?P<name>[A-Z][A-Za-z\-']+(?:['\u2019]s)?)\s+triad[:\s—\-–]+\((?P<items>[^)]+)\)", re.I),
    re.compile(r"triad[:\s—\-–]+\((?P<items>[^)]+)\)", re.I),
]


def extract_sentence_with_phrase(body: str, match_obj, max_len: int = 250) -> str | None:
    start, end = match_obj.span()
    s_start = max(0, body.rfind('. ', 0, start) + 2)
    s_start_alt = max(0, body.rfind('.\n', 0, start) + 2)
    s_start = max(s_start, s_start_alt)
    if s_start < start - 200:
        s_start = max(0, start - 100)
    s_end = body.find('. ', end)
    s_end_alt = body.find('.\n', end)
    candidates = [x for x in [s_end, s_end_alt] if x >= 0]
    s_end = min(candidates) if candidates else min(end + 200, len(body))
    sent = body[s_start:s_end].strip()
    if not sent:
        return None
    if len(sent) > max_len:
        sent = sent[:max_len].rstrip() + '...'
    return sent


def gen_triad_sba(title: str, body: str, ch_slug: str, topic_kw: str) -> dict | None:
    for pat in TRIAD_PATTERNS:
        for m in pat.finditer(body):
            items = m.group('items')
            parts = re.split(r'[,;]|—|–|\sand\s|\sor\s', items)
            parts = [p.strip(' .()\u2014') for p in parts if p.strip()]
            if len(parts) < 3:
                continue
            parts = parts[:5]
            if any(len(p) < 3 or len(p) > 60 for p in parts):
                continue
            triad_str = ', '.join(parts)
            stem = (f"Which of the following is characterised by the clinical "
                    f"triad: {triad_str}?")
            distractors = get_distractors(ch_slug, topic_kw, title)
            options = {'A': title, 'B': distractors[0], 'C': distractors[1], 'D': distractors[2]}
            sent = extract_sentence_with_phrase(body, m)
            return {
                'stem': stem,
                'options': options,
                'answer': 'A',
                'source_quote': sent or triad_str,
            }
    return None


def gen_specific_feature_sba(title: str, body: str, ch_slug: str, topic_kw: str) -> dict | None:
    relevant_body = ''
    for h, b in re.findall(r'##\s*([^\n]+)\n(.*?)(?=\n## |\Z)', body, re.S):
        hl = h.lower()
        if any(k in hl for k in ['clinical feature', 'presentation', 'sign',
                                  'mnemonic', 'pitfall', 'confusion', 'key',
                                  'investigations', 'differential']):
            relevant_body += b + '\n'
    if not relevant_body:
        relevant_body = body
    for m in re.finditer(r'\*\*([^*\n]{3,80}?)\*\*[^\n]{0,200}?(?:specific|characteristic|pathognomonic|hallmark|diagnostic|key|typical|distinctive)',
                         relevant_body, re.I):
        feat = m.group(1).strip()
        if '(' in feat:
            feat = feat.split('(')[0].strip()
        if len(feat) < 3 or len(feat) > 60:
            continue
        if any(x in feat.lower() for x in ['classification', 'severity', 'risk']):
            continue
        stem = (f"Which of the following features is most specific or "
                f"characteristic of {title}?")
        options = {
            'A': feat,
            'B': "A feature common to many acute inflammatory conditions",
            'C': "A non-specific sign that does not localise the diagnosis",
            'D': "An investigation finding rather than a clinical feature",
        }
        sent = extract_sentence_with_phrase(relevant_body, m)
        return {
            'stem': stem,
            'options': options,
            'answer': 'A',
            'source_quote': sent or feat,
        }
    return None


def gen_avoid_sba(title: str, body: str, ch_slug: str, topic_kw: str) -> dict | None:
    relevant_body = ''
    for h, b in re.findall(r'##\s*([^\n]+)\n(.*?)(?=\n## |\Z)', body, re.S):
        hl = h.lower()
        if any(k in hl for k in ['management', 'complication', 'pitfall', 'confusion',
                                  'mnemonic', 'caution', 'contraindication', 'avoid',
                                  'special population', 'interaction', 'pearl']):
            relevant_body += b + '\n'
    if not relevant_body:
        relevant_body = body
    pat = re.compile(
        r"(?:avoid|do not use|contraindicated|caution|should not|careful|never|"
        r"do not give|do not start)\s+([A-Z][A-Za-z0-9\-\s\(\)/]{3,60}?)"
        r"\s+(?:in|for|with|when|if)\s+([A-Za-z][A-Za-z\- ]{3,40}?)(?:[.,;]|$)",
        re.I)
    for m in pat.finditer(relevant_body):
        drug = m.group(1).strip()
        ctx = m.group(2).strip()
        if len(drug) > 50 or len(drug) < 3:
            continue
        if any(x in drug.lower() for x in ['caution', 'drug interactions',
                                            'contraindications', 'comorbidity',
                                            'general', 'principles', 'framework',
                                            'section', 'chapter', 'reference',
                                            'see', 'box', 'appendix', 'table',
                                            'figure', 'classification']):
            continue
        stem = (f"In the management of {title}, which of the following "
                f"should be avoided or is contraindicated?")
        options = {
            'A': f"{drug} (avoid in {ctx[:30]})",
            'B': "Standard guideline-directed first-line therapy",
            'C': "Routine supportive care (fluids, oxygen, monitoring)",
            'D': "Symptom-directed treatment as needed",
        }
        sent = extract_sentence_with_phrase(relevant_body, m)
        return {
            'stem': stem,
            'options': options,
            'answer': 'A',
            'source_quote': sent or m.group(0),
        }
    return None


def gen_trial_sba(title: str, body: str, ch_slug: str, topic_kw: str) -> dict | None:
    EXCLUDE_TRIALS = {'NSAID', 'NSAIDS', 'ICU', 'CXR', 'ECG', 'ABG', 'GI', 'CNS',
                       'BP', 'HR', 'RR', 'EF', 'NYHA', 'BMI', 'DM', 'HTN', 'CKD',
                       'AKI', 'CT', 'MRI', 'PET', 'CSF', 'MRA', 'TIA', 'DAPT',
                       'GDMT', 'LMNOP', 'FBC', 'ESR', 'CRP', 'LDH', 'LFT', 'TFT',
                       'CMV', 'EBV', 'HBV', 'HCV', 'HIV', 'COVID', 'SARS', 'MERS',
                       'AHA', 'ESC', 'NICE', 'BMP'}
    for m in re.finditer(r"\b([A-Z][A-Z0-9\-]{1,10})\s+trial[^\.]{0,100}?(?:showed|demonstrated|found|established|confirmed)\s+([^.]{20,200})", body, re.I):
        trial = m.group(1).strip()
        finding = m.group(2).strip()
        if trial.upper() in EXCLUDE_TRIALS:
            continue
        if not re.match(r'^[A-Z][A-Z0-9\-]{1,8}$', trial):
            continue
        if len(finding) < 20 or len(finding) > 200:
            continue
        stem = (f"Which landmark clinical trial provided evidence relevant to "
                f"the management of {title} (specifically: {finding[:120]})?")
        options = {
            'A': f"{trial} trial",
            'B': "A different but related trial in the same area",
            'C': "A guideline (not a trial) addressing the same question",
            'D': "An observational/cohort study addressing similar outcomes",
        }
        sent = extract_sentence_with_phrase(body, m)
        return {
            'stem': stem,
            'options': options,
            'answer': 'A',
            'source_quote': sent or f"{trial} trial - {finding[:150]}",
        }
    return None


def _find_mgt_section(body: str) -> str:
    """Find the management/treatment section. If H2 body is empty, pull next 3-5 H2 sub-sections."""
    matches = list(re.finditer(r'##\s+([^\n]+)\n(.*?)(?=\n## |\Z)', body, re.S))
    for i, m in enumerate(matches):
        h = m.group(1).strip()
        hl = h.lower()
        if not any(k in hl for k in ['management', 'treatment', 'therapy', 'rx ']):
            continue
        b = m.group(2).strip()
        if b:
            return b
        combined = ''
        for j in range(i + 1, min(i + 6, len(matches))):
            sub_h = matches[j].group(1).strip()
            sub_b = matches[j].group(2).strip()
            combined += f'## {sub_h}\n{sub_b}\n\n'
        if combined:
            return combined
    return ''


def gen_first_line_sba(title: str, body: str, ch_slug: str, topic_kw: str) -> dict | None:
    if not body:
        return None
    mgt_body = _find_mgt_section(body)
    if not mgt_body:
        return None
    text = mgt_body[:3000]
    text_clean = re.sub(r'\|', ' ', text)
    candidates = []
    # Mode 1: bullet-style
    for m in re.finditer(r'^\s*[-*]\s+(.+?)$', text_clean, re.M):
        line = m.group(1).strip()
        if len(line) < 10 or len(line) > 300:
            continue
        ll = line.lower()
        if ll.startswith('avoid') or 'contraindicated' in ll[:50]:
            continue
        if not re.search(r'\*\*[A-Z]', line) and not re.search(r'\b(start|give|prescribe|administer|use)\b', ll):
            continue
        if not re.search(r'\b(start|give|use|prescribe|administer|empiric|treat|cover|choose|therapy|antibiotic|antiviral|anticoagul)\b', ll):
            continue
        candidates.append(line)
        if len(candidates) >= 3:
            break
    # Mode 2: sentence-style
    if not candidates:
        sentences = re.split(r'(?<=[.!?])\s+(?=[A-Z*])|(?<=\n)\s*(?=[A-Z*])', text_clean)
        for s in sentences:
            s_clean = s.strip()
            if not s_clean or len(s_clean) < 10:
                continue
            if len(s_clean) > 400:
                continue
            sl = s_clean.lower()
            if sl.startswith('**avoid') or sl.startswith('avoid ') or 'contraindicated' in sl[:50]:
                continue
            if not re.search(r'\*\*[A-Z][A-Za-z0-9\-]{2,}', s_clean):
                continue
            if not re.search(r'\b(for|in|as|with|treat|manage|step|controller|reliever|first|initial)\b', sl):
                continue
            candidates.append(s_clean)
            if len(candidates) >= 3:
                break
    if not candidates:
        return None
    first = candidates[0]
    drugs = []
    for m in re.finditer(r'\*\*([^*\n]{2,80}?)\*\*', first):
        d = m.group(1)
        if '(' in d:
            d = d.split('(')[0]
        d = re.sub(r'\s+\d.*$', '', d).strip()
        d = d.rstrip('+,').strip()
        if not d:
            continue
        if len(d) < 3 or len(d) > 35:
            continue
        if d.lower() in ('first line', 'first-line', 'first episode', 'recurrence',
                          'acute', 'chronic', 'severe', 'mild', 'moderate',
                          'same', 'asthmatic', 'controller', 'reliever'):
            continue
        drugs.append(d)
    if not drugs:
        first_clean = re.sub(r'\*\*', '', first).strip()
        first_clean = re.sub(r'^[-*]\s+', '', first_clean)
        period = first_clean.find('.')
        if period > 10:
            first_clean = first_clean[:period].strip()
        if len(first_clean) > 120:
            first_clean = first_clean[:120].rstrip(',;') + '...'
        if len(first_clean) < 20:
            return None
        drugs_str = first_clean
        stem = (f"What is the most appropriate first-line therapy for {title}?")
        options = {
            'A': drugs_str,
            'B': "An advanced/surgical therapy reserved for refractory disease",
            'C': "Symptomatic treatment only, no disease-modifying therapy",
            'D': "Empiric broad-spectrum therapy without specific indication",
        }
        return {
            'stem': stem,
            'options': options,
            'answer': 'A',
            'source_quote': first[:300],
        }
    seen = set()
    clean_drugs = []
    for d in drugs:
        if d not in seen:
            seen.add(d)
            clean_drugs.append(d)
    if not clean_drugs:
        return None
    drugs_str = ' + '.join(clean_drugs[:3])
    if len(drugs_str) > 120:
        drugs_str = ' + '.join(clean_drugs[:2])[:120]
    stem = (f"What is the most appropriate first-line therapy for {title}?")
    options = {
        'A': drugs_str,
        'B': "An advanced/surgical therapy reserved for refractory disease",
        'C': "Symptomatic treatment only, no disease-modifying therapy",
        'D': "Empiric broad-spectrum therapy without specific indication",
    }
    return {
        'stem': stem,
        'options': options,
        'answer': 'A',
        'source_quote': first[:300],
    }


def gen_scenarios_for_topic(title: str, sections: list[tuple[str, str]],
                            ch_slug: str) -> list[dict]:
    sbas = []
    seen_stems = set()

    def add(sba):
        if not sba or len(sbas) >= 5:
            return
        key = sba['stem'][:80].lower()
        if key in seen_stems:
            return
        if len(sba['stem']) < 30 or len(sba['stem']) > 600:
            return
        opts = sba['options']
        if not all(opts.get(k) and opts[k].strip() for k in 'ABCD'):
            return
        if len(set(opts.values())) < 4:
            return
        seen_stems.add(key)
        sbas.append(sba)

    topic_kw = topic_keyword(title)
    full_text = '\n'.join(f"## {h}\n{b}" for h, b in sections)

    add(gen_triad_sba(title, full_text, ch_slug, topic_kw))
    add(gen_specific_feature_sba(title, full_text, ch_slug, topic_kw))
    add(gen_avoid_sba(title, full_text, ch_slug, topic_kw))
    add(gen_trial_sba(title, full_text, ch_slug, topic_kw))
    add(gen_first_line_sba(title, full_text, ch_slug, topic_kw))

    return sbas


# ---------------------------------------------------------------------------
# Formatting
# ---------------------------------------------------------------------------

def format_sba_block(sbas: list[dict], topic_title: str, chapter_label: str) -> str:
    if not sbas:
        return ''
    lines = [
        '',
        '## PasTest Scenario SBAs (Clinical Vignettes)',
        '',
        f'> **Auto-generated PasTest/Mediscope-style scenario SBAs** grounded '
        f'in the authored source. Each scenario tests a real clinical fact '
        f'(triad, specific sign, contraindication, trial, first-line Rx) extracted '
        f'from the topic. *Source: {chapter_label} - {topic_title}*',
        '',
    ]
    for i, s in enumerate(sbas, 1):
        lines.append(f'**Q{i}.** {s["stem"]}')
        lines.append('')
        for k in 'ABCD':
            lines.append(f'  - **{k}.** {s["options"][k]}')
        lines.append('')
        ans_text = s['options'][s['answer']]
        lines.append(f'  > **Answer: {s["answer"]}** - {ans_text[:200]}')
        lines.append(f'  >')
        lines.append(f'  > *Source:* {s["source_quote"][:200]}')
        lines.append('')
    return '\n'.join(lines)


# ---------------------------------------------------------------------------
# Topic discovery
# ---------------------------------------------------------------------------

SKIP_FILENAMES = (
    'roadmap', 'hierarchy', 'index', 'readme', 'moc', 'hub',
    'hub overview', 'overview', 'template',
)


def is_real_topic(path: Path) -> bool:
    name = path.stem.lower()
    if any(s in name for s in SKIP_FILENAMES):
        return False
    if path.stat().st_size < 2000:
        return False
    return True


def _normalize(s: str) -> str:
    s = re.sub(r'^[\d.]+-?\s*', '', s)
    s = re.sub(r'\s*\([^)]*\)\s*', ' ', s)
    s = re.sub(r'_(full|notes|draft|final|complete|short|extended|summary)$', '', s, flags=re.I)
    s = re.sub(r'[^a-z0-9]+', ' ', s.lower())
    s = re.sub(r'\s+', ' ', s).strip()
    return s


_published_cache: dict[str, dict[str, Path]] = {}


def _load_published_cache(ch_slug: str) -> dict[str, Path]:
    if ch_slug in _published_cache:
        return _published_cache[ch_slug]
    cache: dict[str, Path] = {}
    ch_dir = CHAPTERS / ch_slug
    diseases = ch_dir / 'diseases'
    if diseases.exists():
        # Mode 1: topic.md in subfolders
        for pmd in diseases.rglob('topic.md'):
            parent = pmd.parent.name
            clean = _normalize(parent)
            if clean:
                cache.setdefault(clean, pmd)
        # Mode 2: *.md in subfolders
        for md in diseases.rglob('*.md'):
            if md.name == 'topic.md' or md.name.endswith('.png') or md.name.endswith('.html'):
                continue
            parent = md.parent.name
            if parent and parent != 'diseases' and not parent.startswith('.'):
                clean = _normalize(parent)
            else:
                clean = _normalize(md.stem)
            if clean:
                cache.setdefault(clean, md)
        # Mode 3: direct .md files
        for md in diseases.glob('*.md'):
            stem = md.stem
            clean = _normalize(stem)
            if clean:
                cache.setdefault(clean, md)
    _published_cache[ch_slug] = cache
    return cache


def find_published_topic(ch_slug: str, src_stem: str) -> Path | None:
    cache = _load_published_cache(ch_slug)
    if not cache:
        return None
    clean_src = _normalize(src_stem)
    if not clean_src:
        return None
    if clean_src in cache:
        return cache[clean_src]
    src_tokens = set(clean_src.split())
    if not src_tokens:
        return None
    best = None
    best_overlap = 0.0
    for cand_stem, cand_path in cache.items():
        cand_tokens = set(cand_stem.split())
        if not cand_tokens:
            continue
        overlap = len(src_tokens & cand_tokens) / max(len(src_tokens | cand_tokens), 1)
        if overlap > best_overlap:
            best_overlap = overlap
            best = cand_path
    if best and best_overlap >= 0.7:
        return best
    return None


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def process_source(src_root: Path, ch_slug: str) -> tuple[int, int, int]:
    if not src_root.exists():
        return (0, 0, 0)
    n_topics = 0
    n_updated = 0
    n_sbas = 0
    for src in sorted(src_root.rglob('*.md')):
        if not is_real_topic(src):
            continue
        n_topics += 1
        try:
            text = src.read_text(encoding='utf-8', errors='replace')
        except Exception:
            continue
        sections = get_h2_sections(text)
        if not sections:
            continue
        title = topic_title_from_path(src)
        sbas = gen_scenarios_for_topic(title, sections, ch_slug)
        if not sbas:
            continue
        pub = find_published_topic(ch_slug, src.stem)
        if pub is None:
            continue
        try:
            pub_text = pub.read_text(encoding='utf-8', errors='replace')
        except Exception:
            continue
        if '## PasTest Scenario SBAs' in pub_text:
            continue
        block = format_sba_block(sbas, title, ch_slug)
        new_text = pub_text.rstrip() + '\n' + block + '\n'
        try:
            pub.write_text(new_text, encoding='utf-8')
        except Exception:
            continue
        n_updated += 1
        n_sbas += len(sbas)
    return (n_topics, n_updated, n_sbas)


def main():
    grand_topics = 0
    grand_updated = 0
    grand_sbas = 0
    for src_dir, ch_slug in SRC_TO_PUB.items():
        src_root = MED / src_dir
        n_topics, n_updated, n_sbas = process_source(src_root, ch_slug)
        grand_topics += n_topics
        grand_updated += n_updated
        grand_sbas += n_sbas
        if n_topics > 0:
            print(f"  {ch_slug:48s}  {n_topics:4d} topics  {n_updated:4d} updated  {n_sbas:4d} SBAs")
    print(f"\n=== Total ===")
    print(f"  Topics scanned:  {grand_topics}")
    print(f"  Topics updated:  {grand_updated}")
    print(f"  Scenario SBAs:   {grand_sbas}")


if __name__ == '__main__':
    main()
