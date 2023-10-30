from survey import AnonymousSurvey

# Define a question and make a survey

question = "What language did you learn first to speak?"
language_survey = AnonymousSurvey(question)

# Show the question and store responses to the question.
language_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input('Language:')
    if response == 'q':
        break
    language_survey.store_response(response)

# Show the survey results
print('\nThank you everyone who participated in survey!')
language_survey.show_results()