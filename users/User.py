class User:
      
      def __init__(self, name, email, drivers_licence, number):
            self.name = name
            self.email = email
            self.drivers_license = drivers_licence
            self.number = number 
            
      def add_post(self):
        self.all_posts = []
        entry = True
        while entry:
            print("""
            1. Create a post
            2. Quit
                """)
            promt_user = input(f"Make Selection: ")

            if promt_user == "1":
                    
                post_added = input(f"Make post here: ")
                self.all_posts.append([post_added])
                    
                
            elif promt_user == "2":
                print("\n No more entries added. Goodbye")
                break
                
                
                    
            print(self.all_posts)
                # elif entry != "":
                #     print("\n Not valid choice try again")
                #     break
                
                        
            # for i in range(5):
            #     entry = input(f"Make post here: ")
            #     self.all_posts.append(entry)
            #     print(self.all_posts)
            
            
            
            
            
      
      def __str__(self):
            return (f"{self.name} , {self.email} , {self.drivers_license} , {self.number}")



# Gary = User("Gary", "@gmail", "1234567", "000-000-0000")
# print(Gary.add_post())



            








# raven = User("Raven", "@gmail", "123", "323-323-3231")
# print(raven.add_post())