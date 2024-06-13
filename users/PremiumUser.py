from User import User


class PremiumUser(User):
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






    def __str__(self):
        return (f"{self.name} , {self.email} , {self.drivers_license} , {self.number}")
    

Gary = PremiumUser("Gary", "@gmail", "1234567", "000-000-0000")
print(Gary.add_post())
