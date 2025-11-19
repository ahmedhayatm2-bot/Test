#4. Movie Ticket Booking Simulation
# Simulate a movie theater booking system that:
# Shows a list of available movie titles, showtimes, and seat prices.
# Asks the user to choose a movie and number of tickets.
# Confirms total price and asks if they want to book another movie.
# Ends when they say “no” and displays total bookings and cost.
# Skills practiced: loops, input, conditionals, calculations, nested dictionaries

movies = {
    "1": {"movie1": "inception", "show_time": "4:00pm", "seat_price": 15.99},
    "2": {"movie2": "only you", "show_time": "6:00pm", "seat_price": 15.99},
    "3":  {"movie3": "life", "show_time": "8:00pm", "seat_price": 15.99}
}

total_cost = 0.00
booking_log = ""

while True:
    print("\n--- Available Movies---") # Fixed the \n typo
    for movie_num, data in movies.items():
        title_key = f"movie{movie_num}"
        print(f"[{movie_num}]: {data[title_key]} at {data['show_time']} (${data['seat_price']:.2f})")
    print("------------------------")
    
    movie_choice = input("Enter movie number (1, 2, or 3) or type 'no' to finish: ").lower()
    
    if movie_choice == "no":
        break
        
    if movie_choice in movies:
        current_movie = movies[movie_choice]
        print(f"You selected: {current_movie[f'movie{movie_choice}']}")

        # --- TICKET LOGIC STARTS HERE (CORRECTLY PLACED) ---
        tickets_input = input("How many tickets do you want to book? ")
        
        if tickets_input.isdigit():
            num_tickets = int(tickets_input)
            
            # --- START OF CALCULATION & LOGGING ---
            price = current_movie['seat_price'] 
            subtotal = num_tickets * price
            
            print(f"Total price for {num_tickets} ticket(s) is: ${subtotal:.2f}")

            confirm = input("Confirm booking? (yes/no): ").lower()
            
            if confirm == "yes":
                total_cost = total_cost + subtotal
                movie_title = current_movie[f'movie{movie_choice}']
                booking_log = booking_log + f"\n- {movie_title} ({current_movie['show_time']}): {num_tickets} tix @ ${subtotal:.2f}"
                print("✅ Booking confirmed!")
            else:
                print("Booking cancelled.")
            # --- END OF CALCULATION & LOGGING ---
            
        else:
            print("Invalid input. Please enter a whole number for tickets.")
        # --- TICKET LOGIC ENDS HERE ---

    else:
        print("Invalid movie number. Please choose 1, 2, or 3.")

# Execution continues here when 'no' is entered
print("Loop finished. Ready to process selected movies.")
# Execution continues here after the 'no' break
print("\n\n========== FINAL BOOKING RECEIPT ==========")

# Conditional to check if the user bought anything
if total_cost > 0:
    print("--- Your Bookings ---")
    
    # Print the accumulated string log
    print(booking_log) 
    
    print("-----------------------------------------")
    
    # Print the final total cost
    print(f"TOTAL COST: .................... ${total_cost:.2f}")
else:
    print("No bookings were made.")
    
print("===========================================\n")