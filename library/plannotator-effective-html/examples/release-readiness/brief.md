# Atlas Mobile 4.8 release-readiness brief

## User and task

A release manager must decide whether Atlas Mobile 4.8 can go to production.

## Required information

- Release candidate and commit
- Release owner
- Four required checks and their current state
- Evidence behind each check
- Open risks and reviewer notes
- Current release decision

## Required behavior

The page starts blocked because the iOS smoke test failed. A reviewer can record a passing rerun. The release state then changes from blocked to ready, and the production-release action becomes available.

## Non-goals

- Starting a real deployment
- Authentication or authorization
- Loading live build data
- Defining the production application's component architecture
- Final product copy for every failure and recovery state
