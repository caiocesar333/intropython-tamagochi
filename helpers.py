
def show_tamagochis(tam_list):
    print("\n ---------- List of Tamagochis ---------- \n")
    for tam in tam_list:
        tam.show_name()
    print("Select one of the above (write the name)")

def show_statistics(tam_list):
    tam_count = 0
    living_count = 0
    total_hunger = 0
    total_health = 0
    total_boredom = 0
    total_exhaustion = 0
    for tam in tam_list:
        tam_count += 1
        st = tam.return_statistics()
        if type(st) is dict:
            if st.get("alive") == True:
                living_count += 1

            total_hunger += st.get("hunger")
            total_health += st.get("health")
            total_boredom += st.get("boredom")
            total_exhaustion += st.get("exhaustion")

    avg_hunger = total_hunger / tam_count
    avg_health = total_health / tam_count
    avg_boredom = total_boredom / tam_count
    avg_exhaustion = total_exhaustion / tam_count

    print("\n ---------- Game Statistics ---------- \n")
    print(f" Number of tamagochis: {tam_count}")
    print(f" Number of living tamagochis: {living_count}")
    print(f" Average hunger: {avg_hunger}")
    print(f" Average health: {avg_health}")
    print(f" Average boredom: {avg_boredom}")
    print(f" Average exhaustion: {avg_exhaustion}")

