from app.core.placa_evaluator import PlacaEvaluatorDFA

def validate_plate(plate:str) -> bool:
    evaluator = PlacaEvaluatorDFA()
    
    
    
    return evaluator.evaluate(plate)
