use alt+c to check items off of lists :3 

- [todo](#todo)
- [incense](#incense)
- [pedo](#pedo)
- [teenpreg](#teenpreg)
- [new-traits](#new-traits)
  - [v-traits](#v-traits)
  - [c-traits](#c-traits)
- [events](#events)
- [new-patrol](#new-patrol)

# todo
MAIN TO-DO:
    - [x] incest (basic)
        - [ ] expand on incest
    - [x] underage mates
    - [ ] pregnancies
        - [ ] underage pregnancy
        - [ ] noncon pregnancy
        - [ ] infertility?
        - [ ] complications?
    - [ ] custom events
        - [ ] heat/rut
        - [ ] groomer relationship events
        - [ ] patrol rape
        - [ ] noncon relationship events
    - [ ] longform events (spread out over several moons)
    - [ ] toggle for normalized grooming/incest
        - [ ] toggle to disable explicit events
    - [ ] new patrol type for SEX

# incense
INCEST:
    - [x] allow incest
    - [ ] custom incestuous relationship events
    - [ ] incestuous trait/skill? that can be randomly aquired by cats with c personality traits
    - [ ] limit incestuous relationships to cats w/ incest trait when problematic setting is off
    - [ ] investigate anti-inbreeding family size limits on pregnancies

# pedo
UNDERAGE ROMANCE
    - [x] allow underage mates
    - [x] allow mentor x apprentice

# teenpreg
UNDERAGE PREGNANCIES:
    - [x] allow underage pregnancy
    - [x] kit chances
    - [x] mortality rate
    - [ ] flavor text
      - [ ] announcement flavor text
      - [ ] litter-guess flavor text
      - [ ] birth flavor text
      - [ ] death flavor text
    - [ ] pregnancy complications
      - [ ] miscarriages
      - [ ] death mid-pregnancy

# new-traits
add (something) that compiles groups of traits to be compatible with certain ages, roles, etc, and that will trigger exclusive events so that some cats act creepier than others & normal cats dont act ooc
    - [ ] implement trait groups
    - [ ] add custom compatibility (dont use pre-built compatibility, create a new function to parse the specific constraints)
      - [ ] between v & c trait groups
      - [ ] c traits x underage cats
      - [ ] certain roles w/ c traits x v traits
    - [ ] add custom events for trait groups

## v-traits
    childish
    nervous
    insecure
    oblivious
    meek
        -kit-specific:
        shy
        attention-seeker
        fearless
        quiet
        self-conscious
        sweet
        polite
        *all kits will be targeted by creeps, but kits with v traits will have a higher chance of being successfully groomed*
## c-traits
    charismatic
    shameless
    sneaky
    strange
    arrogant ?
    cunning
    obsessive
        -kit-specific:
        manipulative
        leader-like
        smug
        *might add some unique events for evil kits kitconning other kits. higher likelyhood of incest*

# events
  - (long) obsessive personality cat targets a cat to repeatedly rape & eventually kidnap or murder
    - several outcomes including preg, kidnap, murder, & stolkholm
  - tnr
    - rare implied human on feral?
    - infertility mechanic?
  - noncon events
    - random chance to trigger on timeskips, affected by personalities
    - asexuality trait that doubles chance of marital rape
  - seasonal heat/rut events
    - during newleaf, timeskip events implying cats are in heat can occur (misc or relationships). may be both vague and explicit.
  - patrol events
    - noncon events on patrols where one or more cats has a creep trait
      - higher likelyhood if only 2 cats, even higher if the victim is young.
      - gangbang/orgy event for >2 creepy cats
      - failure chance may result in future consequences/exile
  - exile/consequences
    - victims with bold traits might report their rape to the clan
    - if the leader/dep is sympathetic, the offending cat may be exiled
    - if the leader/dep is equally creepy, the offending cat stays
      - in this case, mates/family of the victim may take justice into their own hands.

# new-patrol
unlike lifegen dates, more like smashing dolls together.
  - [ ] create/modify new patrol screen
  - [ ] proceed/antagonize indicates consent
  - [ ] proceed fails if relationship isnt high enough
  - [ ] if possible, disable antagonize button if no creepy cats are on the patrol
  - [ ] number of creepy cats must outnumber or equal the number of victims for antagonize to succeed
  - [ ] antagonize might fail if the other cat doesnt have a victim type personality
  - [ ] antagonize decreases the relationship between agressor & victim
  - [ ] result event strings:
    - [ ] setup event
    - [ ] consensual proceed result
    - [ ] proceed failure (rejection) result
    - [ ] noncon antagonize result
    - [ ] antagonize failure