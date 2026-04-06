class Unification:
    def __init__(self):
        self.substitution = {}

    
    def is_variable(self, x):
        return isinstance(x, str) and x.islower()

    
    def unify(self, x, y):
        if x == y:
            return True

        elif self.is_variable(x):
            return self.unify_var(x, y)

        elif self.is_variable(y):
            return self.unify_var(y, x)

        elif isinstance(x, list) and isinstance(y, list) and len(x) == len(y):
            for i in range(len(x)):
                if not self.unify(x[i], y[i]):
                    return False
            return True

        else:
            return False

   
    def unify_var(self, var, x):
        if var in self.substitution:
            return self.unify(self.substitution[var], x)

        elif x in self.substitution:
            return self.unify(var, self.substitution[x])

        else:
            self.substitution[var] = x
            return True



def parse_expression(expr):
    expr = expr.replace("(", " ").replace(")", " ").replace(",", " ")
    return expr.split()



if __name__ == "__main__":
    u = Unification()

    print("Enter first expression (e.g., P(x, a)):")
    expr1 = input()

    print("Enter second expression (e.g., P(b, y)):")
    expr2 = input()

    e1 = parse_expression(expr1)
    e2 = parse_expression(expr2)

    if u.unify(e1, e2):
        print("\nUnification Successful!")
        print("Substitutions:")
        for k, v in u.substitution.items():
            print(f"{k} -> {v}")
    else:
        print("\nUnification Failed!")