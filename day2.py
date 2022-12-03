class Strategy:
    def __init__(self, input: str):
        choices = input.split()
        self.opponent_choice = choices[0]
        #self.my_choice = choices[1]
        #self._calculate_result()
        self._translate_result(choices[1])
        self._calculate_choice()
        self._calculate_score()
    
    def _translate_result(self, encoded_result: str):
        if encoded_result == "X":
            self.result = "L"
        elif encoded_result == "Y":
            self.result = "D"
        # Z
        else:
            self.result = "W"
        
    def _calculate_choice(self):
        if self.opponent_choice == "A":
            if self.result == "W":
                self.my_choice = "Y"
            elif self.result == "D":
                self.my_choice = "X"
            else:
                self.my_choice = "Z"

        elif self.opponent_choice == "B":
            if self.result == "W":
                self.my_choice = "Z"
            elif self.result == "D":
                self.my_choice = "Y"
            else:
                self.my_choice = "X"

        else:
            if self.result == "W":
                self.my_choice = "X"
            elif self.result == "D":
                self.my_choice = "Z"
            else:
                self.my_choice = "Y"
    
    def _calculate_result(self):
        self.result = "INVALID"
        if self.opponent_choice == 'A':
            if self.my_choice == 'X':
                self.result = "D"
            elif self.my_choice == "Y":
                self.result = "W"
            else:
                self.result = "L"

        elif self.opponent_choice == 'B':
            if self.my_choice == 'X':
                self.result = "L"
            elif self.my_choice == "Y":
                self.result = "D"
            else:
                self.result = "W"
        # C
        else:
            if self.my_choice == 'X':
                self.result = "W"
            elif self.my_choice == "Y":
                self.result = "L"
            else:
                self.result = "D"
                
    def _calculate_score(self):
        result_score = 0
        if self.result == "W":
            result_score = 6
        elif self.result == "D":
            result_score = 3
        else:
            result_score = 0
        
        shape_score = 0
        if self.my_choice == "X":
            shape_score = 1
        elif self.my_choice == "Y":
            shape_score = 2
        else:
            shape_score = 3
        
        self.score = result_score + shape_score



strategy_guide_list = []

with open("input/day2_input.txt") as f:
    strategy_guide_list = f.readlines()
    
strategies = [Strategy(item) for item in strategy_guide_list]
total_score = 0
for strategy in strategies:
    total_score += strategy.score

print(f"Total score: {total_score}")

