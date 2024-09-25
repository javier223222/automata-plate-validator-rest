from app.core.placa_evaluator import PlacaEvaluatorDFA

def test_is_valid_plate():
    evaluator = PlacaEvaluatorDFA()
    assert evaluator.evaluate("DSZ-999-Z") == True
    assert evaluator.evaluate("DC-9999-Z") == True
    assert evaluator.evaluate("99-AYZ-99") == True
    assert evaluator.evaluate("Z-999-ZSZ") == True
    assert evaluator.evaluate("CS-999Z-Z") == True
    
def test_is_invalid_plate():
    evaluator = PlacaEvaluatorDFA()
    assert evaluator.evaluate("DSZ-999-ZZ") == False
    assert evaluator.evaluate("DC-9999-ZZ") == False
    assert evaluator.evaluate("99-AYZ-999") == False
    assert evaluator.evaluate("Z-999-ZSZZ") == False
    assert evaluator.evaluate("CS-999Z-ZZ") == False