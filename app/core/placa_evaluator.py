class PlacaEvaluatorDFA:
    def __init__(self):
        self.state="q0"
        self.final_states = {'q9', 'q18'} # Estados finales
    def is_valid_letter(self,char):
        return char.isalpha() and char not in {"I","O","Q"}  and  char.upper()==char# Verifica si es una letra y no es I,O,Q
    def is_valid_number(self,char):
        return char.isdigit() and 0 <= int(char) <= 9 # Verifica si es un número entre 0 y 9
    def transition(self,current_state,char): # Función de transición
        if current_state=="q0":
            
            if self.is_valid_letter(char):   # Verifica si es una letra
                return "q10" # Cambia al estado q10
            elif self.is_valid_number(char):
                
                return "q1" # Cambia al estado q1
        elif current_state=="q1": # Estado q1
            if self.is_valid_number(char): # Verifica si es un número
                return "q2" # Cambia al estado q2
        elif current_state=="q2": # Estado q2
            if char == "-": # Verifica si es un guión
                return "q3" # Cambia al estado q3
        elif current_state=="q3": # Estado q3
            if self.is_valid_letter(char): # Verifica si es una letra
                return "q4" # Cambia al estado q4
        elif current_state=="q4": # Estado q4
            if self.is_valid_letter(char): # Verifica si es una letra
                return "q5" # Cambia al estado q5
        elif current_state=="q5": # Estado q5
            if self.is_valid_letter(char): # Verifica si es una letra
                return "q6" # Cambia al estado q6
        elif current_state=="q6": # Estado q6
            if char =="-":  # Verifica si es un guión
                return "q7" # Cambia al estado q7
        elif current_state=="q7": # Estado q7
            if self.is_valid_number(char):  # Verifica si es un número
                return "q8" # Cambia al estado q8
        elif current_state=="q8": # Estado q8
            if self.is_valid_number(char): # Verifica si es un número
                return "q9" # Cambia al estado q9 estado final
        elif current_state == "q10":
             # Estado q10
            if char == "-": # Verifica si es un guión
                return "q11" # Cambia al estado q11
            elif self.is_valid_letter(char):
                 # Verifica si es una letra
                return "q19"    # Cambia al estado q19 
        elif current_state == "q11": # Estado q11
            if self.is_valid_number(char): # Verifica si es un número
                return "q12" # Cambia al estado q12
        elif current_state == "q12": # Estado q12
            if self.is_valid_number(char): # Verifica si es un número
                return "q13" # Cambia al estado q13
        elif current_state == "q13": # Estado q13
            if self.is_valid_number(char): # Verifica si es un número
                return "q14" # Cambia al estado q14
        elif current_state == "q14":     # Estado q14
            if char == "-": # Verifica si es un guión
                return "q15" # Cambia al estado q15
        elif current_state == "q15": # Estado q15
            if self.is_valid_letter(char): # Verifica si es una letra
                return "q16" # Cambia al estado q16
        elif current_state == "q16": # Estado q16
            if self.is_valid_letter(char):  # Verifica si es una letra
                return "q17" # Cambia al estado q17
        elif current_state == "q17": # Estado q17
            if self.is_valid_letter(char): # Verifica si es una letra
                return "q18" # Cambia al estado q18 estado final
        elif current_state == "q19": # Estado q19
            if char == "-": # Verifica si es un guión
                return "q20" # Cambia al estado q20
            elif self.is_valid_letter(char): # Verifica si es una letra
                return "q25"    # Cambia al estado q25
        elif current_state == "q20":  # Estado q20
            if self.is_valid_number(char): # Verifica si es un número
                return "q21" # Cambia al estado q21
        elif current_state == "q21": # Estado q21
            if self.is_valid_number(char): # Verifica si es un número
                return "q22" # Cambia al estado q22
        elif current_state == "q22": # Estado q22
            if self.is_valid_number(char): # Verifica si es un número
                return "q23" # Cambia al estado q23
        elif current_state == "q23":
             # Estado q23
            if self.is_valid_number(char) or self.is_valid_letter(char): # Verifica si es un número
                return "q24"    # Cambia al estado q24
             
        elif current_state == "q24": # Estado q24
            if char == "-":  # Verifica si es un guión
                return "q17" # Cambia al estado q17
        elif current_state == "q25":     # Estado q25
            if char == "-": # Verifica si es un guión
                return "q26" # Cambia al estado q26
        elif current_state == "q26": # Estado q26
            if self.is_valid_number(char): # Verifica si es un número
                return "q27" # Cambia al estado q27
        elif current_state == "q27": # Estado q27
            if self.is_valid_number(char): # Verifica si es un número
                return "q28" # Cambia al estado q28
        elif current_state == "q28": # Estado q28
            if self.is_valid_number(char): # Verifica si es un número
                return "q24" # Cambia al estado q24
        
        return "invalid" # Estado inválido
    def evaluate(self,plate) -> bool: 
                         # Función de evaluación
        for char in plate:
            self.state=self.transition(self.state,char)
            
            if self.state=="invalid":
                return False
            elif self.state in self.final_states:
                return self.state in self.final_states

        
        
            
        
    
    
        
        
            
            
        

