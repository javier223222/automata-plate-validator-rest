import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.core.placa_evaluator import PlacaEvaluatorDFA

    
def test_is_valid_plate():
    
        evaluator = PlacaEvaluatorDFA()
    
        assert evaluator.evaluate("DSZ-999-Z") == True
        
        
    

      

def test_is_valid_plate_two():
    evaluator = PlacaEvaluatorDFA()
    assert evaluator.evaluate("DC-9999-Z") == True

def test_is_valid_plate_three():
    evaluator = PlacaEvaluatorDFA()
    assert evaluator.evaluate("99-AYZ-99") == True
    

def test_is_valid_plate_four():
    evaluator = PlacaEvaluatorDFA()
    assert evaluator.evaluate("Z-999-ZSZ") == True

    
def test_is_valid_plate_five():
    evaluator = PlacaEvaluatorDFA()
    assert evaluator.evaluate("CS-999Z-Z") == True

    
def test_is_invalid_plate():
    evaluator = PlacaEvaluatorDFA()
    assert evaluator.evaluate("DSZ-999-ZZ") == False


    
    assert evaluator.evaluate("CS-999Z-ZZ") == False


def test_is_invalidad_plate():
    evaluator = PlacaEvaluatorDFA()
    assert evaluator.evaluate("DC-9999-ZZ") == False

def test_is_invalidad_plate_two():
    evaluator = PlacaEvaluatorDFA()
    assert evaluator.evaluate("99-AYZ-999") == False


def test_is_invalidad_plate_three():
    evaluator = PlacaEvaluatorDFA()
    assert evaluator.evaluate("Z-999-ZSZZ") == False

def  test_is_invalidad_plate_four():
    evaluator = PlacaEvaluatorDFA()
    assert evaluator.evaluate("CS-999Z-ZZ") == False

