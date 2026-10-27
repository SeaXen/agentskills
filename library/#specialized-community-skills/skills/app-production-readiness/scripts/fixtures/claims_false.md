# Production review (fixture - every gate claimed PASS, none of it true)

GATES      : A visual PASS | B perf PASS | C polish PASS | D lighthouse PASS | E security PASS | F a11y PASS | G seo PASS | H tests PASS | I reliability PASS | J docs PASS | K observability PASS | L cost PASS | M readme PASS | N logic PASS | O load PASS | P migrations PASS | Q privacy PASS | R i18n PASS | S at PASS | T payments PASS | U quality PASS

This file exists to prove the verifier catches a report that claims everything
passed.  Point `verify_claims.py` at a broken project with this file and the
verdict must be a failure.
