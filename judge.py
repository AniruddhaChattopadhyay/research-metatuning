
from pydantic import BaseModel
from litellm import completion

class AnswerCorrectness(BaseModel):
  correct:bool


response_schema_answer_correctness = {
    "type": "object",
    "properties": {
        "correct": {
            "type": "boolean"
        },
    },
    "required": ["correct"]
}


class Judge:
    def __init__(self,model,structured_output=True)->None:
        self.model = model
        self.structured_output = structured_output

    def prediction(self,query:str,answer1:str,answer2:str)->AnswerCorrectness:
        response_format = None
        if 'gemini' in self.model: 
            response_format = {"type": "json_object", "response_schema": response_schema_answer_correctness}
        else:
            response_format = AnswerCorrectness

        response = completion(model=self.model, messages=[
            {
                'role': 'system',
                'content': '''You are an intellegent maths professor. I will give you 2 answers.
                    One Model answer and one student answer. You determine whether the answer is right or wrong. 
                    Return a json with key are correct and value as True or False depeding on your evaluation. 
                    I will also give you the actual problem, for your reference. Don't solve the problem. 
                    You are just to look at the two answer and judge whether the 2 answers are similar.
                    
                    Also latex formatting doesn't matter as long as the answers are correct.
                    One of the answers can be one word while the other is a bit verbose. That's okay. Just check for if they are actually true.

                    example:
                    Model Answer : 9, Student Answer : The answer of a+b is 9
                    Output: True
                    
                    Here both answers are same since both report 9. Whether both are equally verbose doesn't matter''',
            },
            {
                'role': 'user',
                'content': f'Model Answer : {answer1}, Student Answer : {answer2}, problem : {query}',
            },
        ], 
        response_format=response_format)

        answer_correctness = response.choices[0]['message']['content']
        answer_correctness_obj = AnswerCorrectness.model_validate_json(answer_correctness)
        return answer_correctness_obj