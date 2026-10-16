from pyscript import document

# Python list containing g10 ict club members
club_members = [
"Gavin Ruiz", "Edrian Correa", "Philip Ponce", "Julian Anaque", "Andrik David", "Annika De Vera", "Eliana Daet", "Zecca Zeppola", "Tic Toc Tortora", "Ratio Randall", "Coccinella Cotoletta", "Farfallina Farfallona", "Grissino Gabbiano", "Biscotto Brontolone", "Falena Fettuccina", "Brum Brum Bradipo", "Maestro Mortadella", "Sedia Seppia"
]
club_members.sort()

def check_membership(event):
    # First and last name entered by the user and combine them into one full name
    fname = document.querySelector("#first-name").value.strip()
    lname = document.querySelector("#last-name").value.strip()
    full_name = f"{fname} {lname}"

    # Check whether the full name is in the club members list. 
    is_member = full_name in club_members

    # boolean indexing (True -> 1, False -> 0)
    messages = (f"Please Check if your name is in the list of G10 ICT Club Members:{club_members}. {full_name} is a member.",
                f"Please Check if your name is in the list of G10 ICT Club Members:{club_members}. {full_name} is not a member.")

    print.txt(f"Please Check if your name is in the list of G10 ICT Club Members:{club_members}. {full_name} is a member.")
    
    
    bg_colors = ["#f8d7da", "#d1e7dd"]
    text_colors = ["#721c24", "#155724"]

    index = int(is_member)
    message = messages[index]

    # Update result area UI
    result_div = document.querySelector("#result")
    result_div.innerText = message
    result_div.style.backgroundColor = bg_colors[index]
    result_div.style.color = text_colors[index]