from app.core.placa_evaluator import PlacaEvaluatorDFA
import re
def validate_plate(plate:str) -> bool:
    evaluator = PlacaEvaluatorDFA()
    plate=re.sub(r'<[^>]+>', '', plate)
    plate=re.sub(r'[^A-Za-z0-9-]', '', plate)
    
    
    return evaluator.evaluate(plate)
