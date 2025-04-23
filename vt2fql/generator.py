from vt2fql.vt_extractor import *
from vt2fql.fql_templates import *

class FQLGenerator:
    def __init__(self, ioc: dict):
        self.ioc = ioc
        self.used_fields = []
    
    def generate(self):
        RED = "\033[91m"
        RESET = "\033[0m"
        
        query = []

        for key, value in self.ioc.items():
            if key in FQL_TEMPLATE:
                template = FQL_TEMPLATE[key]
                self.used_fields.append(key)

                # Extract the field part from the template (before the colon or =)
                field = template.split(":")[0].split("=")[0]

                colored_template = template.replace(field, f"{RED}{field}{RESET}")

                if isinstance(value, list):
                    for item in value:
                        if item:
                            query.append(colored_template.format(value=item))
                elif isinstance(value, str) and value.strip():
                    query.append(colored_template.format(value=value))

        return " OR ".join(query) if query else "# No valid FQL fields found"
        
    def explain(self):
        if not self.used_fields:  
            self.generate()

        
        for field in self.used_fields:
            print(f"✔️ Used field: {field}") 
        
                
        
        
                
    
                
        
                
        
