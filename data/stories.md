## story_001
* greet
   - utter_greet

## story 2
* goodbye
    - utter_goodbye

## story 3
* start_quiz
    - action_listtopics

## story 4
* select_topic
    - action_askquestion

## story 5
* answer_question
    - action_validate

## story 6
* goodbye
    - utter_goodbye

## Generated Story -637031665394438183
* greet
    - utter_greet
* start_quiz
    - action_listtopics
* select_topic{"topic": "sports"}
    - slot{"topic": "sports"}
    - action_askquestion
* answer_question{"topic": "golf"}
    - slot{"topic": "golf"}
    - action_validate
    - action_askquestion
* goodbye
    - utter_goodbye

## Generated Story 5397892107427748086
* greet
    - utter_greet
* start_quiz
    - action_listtopics
* select_topic{"topic": "movie"}
    - slot{"topic": "movie"}
    - action_askquestion
* answer_question{"answer": "2"}
    - slot{"answer": "2"}
    - action_validate
    - action_askquestion
* answer_question{"answer": "0"}
    - slot{"answer": "0"}
    - action_validate
* goodbye
    - utter_goodbye

## Generated Story -4073044648581438078
* greet
    - utter_greet
* start_quiz
    - action_listtopics
* select_topic{"topic": "sports"}
    - slot{"topic": "sports"}
    - action_askquestion
* answer_question{"answer": "1"}
    - slot{"answer": "1"}
    - action_validate

## Generated Story 3691144381135596213
* greet
    - utter_greet
* start_quiz
    - action_listtopics
* select_topic{"topic": "sports"}
    - slot{"topic": "sports"}
    - action_askquestion
* answer_question{"answer": "0"}
    - slot{"answer": "0"}
    - action_validate

## Generated Story 794892908448623803
* select_topic{"topic": "science"}
    - slot{"topic": "science"}
    - action_askquestion
* answer_question{"answer": "0"}
    - slot{"answer": "0"}
    - action_askquestion
* goodbye
    - utter_goodbye

## Generated Story 2540329762138369031
* select_topic{"topic": "movie"}
    - slot{"topic": "movie"}
    - action_askquestion
* answer_question{"answer": "2"}
    - slot{"answer": "2"}
    - action_validate
    - action_askquestion
* answer_question{"answer": "eights"}
    - slot{"answer": "eights"}
    - action_validate
    - action_askquestion
* goodbye
    - utter_goodbye


## Generated Story 1383309626285400005
* select_topic{"topic": "sports"}
    - slot{"topic": "sports"}
    - action_askquestion
* answer_question{"answer": "1"}
    - slot{"answer": "1"}
    - action_validate
    - slot{"answer": null}
    - action_askquestion
* answer_question{"answer": "2"}
    - slot{"answer": "2"}
    - action_validate
    - slot{"answer": null}
    - action_askquestion
* answer_question{"answer": "1"}
    - slot{"answer": "1"}
    - action_validate
    - slot{"answer": null}
    - action_askquestion
* answer_question{"answer": "2"}
    - slot{"answer": "2"}
    - action_validate
    - slot{"answer": null}
    - action_askquestion
* goodbye
    - utter_goodbye
    
