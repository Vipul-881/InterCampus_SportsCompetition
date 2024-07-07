import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import mysql.connector
from tkinter import ttk

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("InterBITS Sports Competition Database")
        self.geometry("800x600")  # Set the size of the window

        # Load the background image
        self.background_image = PhotoImage(file="final1.png")

        # Create a label to display the background image
        self.background_label = tk.Label(self, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Create buttons for teams, players, matches, and referees
        self.create_buttons()

    def create_buttons(self):
    # Create a custom style for the buttons
     button_style = ttk.Style()
     button_style.configure("Neon.TButton", foreground="black", background="blue", bordercolor="blue")

    # Buttons for the left side
     team_button = ttk.Button(self, text="Team", command=self.team_window, style="Neon.TButton")
     team_button.grid(row=0, column=0, sticky="ew", padx=10, pady=5)

     player_button = ttk.Button(self, text="Player", command=self.player_window, style="Neon.TButton")
     player_button.grid(row=1, column=0, sticky="ew", padx=10, pady=5)

     match_button = ttk.Button(self, text="Match", command=self.match_window, style="Neon.TButton")
     match_button.grid(row=2, column=0, sticky="ew", padx=10, pady=5)

     referee_button = ttk.Button(self, text="Referee", command=self.referee_window, style="Neon.TButton")
     referee_button.grid(row=3, column=0, sticky="ew", padx=10, pady=5)

    # Buttons for the right side
     q1_button = ttk.Button(self, text="Gold in Sport", command=self.gfors_window, style="Neon.TButton",width=10)
     q1_button.grid(row=0, column=1, sticky="ew", padx=10, pady=5)

     q2_button = ttk.Button(self, text="Matches in Sport", command=self.mfors_window, style="Neon.TButton",width=10)
     q2_button.grid(row=1, column=1, sticky="ew", padx=10, pady=5)

     q3_button = ttk.Button(self, text="Teams from Campus", command=self.tinc_window, style="Neon.TButton",width=10)
     q3_button.grid(row=2, column=1, sticky="ew", padx=10, pady=5)

     q4_button = ttk.Button(self, text="Teams in Sport", command=self.tins_window, style="Neon.TButton",width=10)
     q4_button.grid(row=3, column=1, sticky="ew", padx=10, pady=5)

    # Column configuration to push buttons to the right side
     self.grid_columnconfigure(1, weight=1)



####################################################################################################    
# PLAYER
    def player_window(self):
        window = tk.Toplevel(self)
        window.title("Player")

        add_player_button = tk.Button(window, text="Add Player", command=self.add_player_window)
        add_player_button.pack()

        del_player_button = tk.Button(window, text="Update Player", command=self.del_player_window)
        del_player_button.pack()

    def add_player_window(self):
        # Create window for option 1
        window = tk.Toplevel(self)
        window.title("add player Window")

        labels = ["BITS ID:" ,"Name:"," sportID", "CampusID:", "teamID ",  "Gender:","Height:", "Weight:"]
        self.create_labels_and_entries(window, labels, self.add_player)

    def del_player_window(self):
        
        window = tk.Toplevel(self)
        window.title("delete player Window")

        labels = [ "ID:"]
        self.create_labels_and_entries(window, labels, self.del_player) #CREATE FUNCTION


####################################################################################################
#TEAM
    def team_window(self):
        window = tk.Toplevel(self)
        window.title("Team")

        add_team_button = tk.Button(window, text="Add Team", command=self.add_team_window)
        add_team_button.pack()

        upd_team_button = tk.Button(window, text="Update Team", command=self.upd_team_window)
        upd_team_button.pack()

        del_team_button = tk.Button(window, text="Delete Team", command=self.del_team_window)
        del_team_button.pack()
        

    def add_team_window(self):
        # Create window for option 1
        window = tk.Toplevel(self)
        window.title("add team Window")

        labels = ["team ID ",  "CampusID:", "Name:", "Number of Players:", "Gender:", "SportID:"]
        self.create_labels_and_entries(window, labels, self.add_team)

    def upd_team_window(self):
        
        window = tk.Toplevel(self)
        window.title("update team Window")

        labels = [ "team ID:"]
        self.create_labels_and_entries(window, labels, self.update_team) #CREATE FUNCTION

    def del_team_window(self):
        
        window = tk.Toplevel(self)
        window.title("delete team Window")

        labels = [ "team ID:"]
        self.create_labels_and_entries(window, labels, self.del_team) #CREATE FUNCTION   

####################################################################################################
# MATCH    
    def match_window(self):
        window = tk.Toplevel(self)
        window.title("Match")

        add_match_button = tk.Button(window, text="Add Match", command=self.add_match_window)
        add_match_button.pack()

        upd_match_button = tk.Button(window, text="Update Match", command=self.upd_match_window)
        upd_match_button.pack()

        del_match_button = tk.Button(window, text="Delete Match", command=self.del_match_window)
        del_match_button.pack()
        

    def add_match_window(self):
        # Create window for option 1
        window = tk.Toplevel(self)
        window.title("add match Window")

        labels = ["Match ID:", "Team 1 ID:", "Team 2 ID:", "SportID:", "Date:", "Time:",  "Referee ID:","Gender", "Venue:","Win ID:"]
        self.create_labels_and_entries(window, labels, self.add_match)

    def upd_match_window(self):
        
        window = tk.Toplevel(self)
        window.title("update match Window")

        labels = [ "matchID:","date:","time:"]
        self.create_labels_and_entries(window, labels, self.update_match) #CREATE FUNCTION

    def del_match_window(self):
        
        window = tk.Toplevel(self)
        window.title("delete match Window")

        labels = [ "matchID:"]
        self.create_labels_and_entries(window, labels, self.del_match) #CREATE FUNCTION
####################################################################################################    
# REFEREE    
    
    def referee_window(self):
        window = tk.Toplevel(self)
        window.title("referee")

        add_match_button = tk.Button(window, text="Add referee", command=self.add_referee_window)
        add_match_button.pack()

        upd_match_button = tk.Button(window, text="Update referee", command=self.upd_referee_window)
        upd_match_button.pack()

        
        

    def add_referee_window(self):
        # Create window for option 1
        window = tk.Toplevel(self)
        window.title("add referee Window")

        labels = ["Referee ID:", "SportID:", "Hours:", "Remuneration:","refName" ,"Contact:"]
        self.create_labels_and_entries(window, labels, self.add_referee)

    def upd_referee_window(self):
        
        window = tk.Toplevel(self)
        window.title("update referee Window")

        labels = [ "ID:" , " Hours: "]
        self.create_labels_and_entries(window, labels, self.update_ref) #CREATE FUNCTION
####################################################################################################
    def gfors_window(self):
        window = tk.Toplevel(self)
        window.title("gold for sport")

        labels = [ "sportID:" ]
        self.create_labels_and_entries(window, labels, self.gfors)

    def mfors_window(self):
        window = tk.Toplevel(self)
        window.title("match in sport")

        labels = [ "sportID:" ]
        self.create_labels_and_entries(window, labels, self.mfors)

    def tinc_window(self):
        window = tk.Toplevel(self)
        window.title("teams in campus")

        labels = [ "campusID:" ]
        self.create_labels_and_entries(window, labels, self.tinc)

    def tins_window(self):
        window = tk.Toplevel(self)
        window.title("teams in sport")

        labels = [ "sportID:" ]
        self.create_labels_and_entries(window, labels, self.tins)

    def create_labels_and_entries(self, window, labels, command):
        for i, label_text in enumerate(labels):
            label = tk.Label(window, text=label_text)
            label.grid(row=i, column=0)
            entry = tk.Entry(window)
            entry.grid(row=i, column=1)

        add_button = tk.Button(window, text="Add", command=lambda: command(window))
        add_button.grid(row=len(labels), columnspan=2)
####################################################################################################
#PLAYER

    def add_player(self, window):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="W3124#azd!%",
                database="dbsproj"
            )
            cursor = conn.cursor()

            # Get values from entry widgets
            values = [entry.get() for entry in window.winfo_children() if isinstance(entry, tk.Entry)]

            # Insert data into the database
            cursor.execute("INSERT INTO player (player_name, age, height, weight, gender, campus, bits_id) VALUES (%s, %s, %s, %s, %s, %s, %s)", values)
            conn.commit()

            # Close the connection
            conn.close()

            # Show success message
            messagebox.showinfo("Success", "Player added successfully!")

            # Close the window after successful insertion
            window.destroy()

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def del_player(self, window):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="W3124#azd!%",
                database="dbsproj"
            )
            cursor = conn.cursor()
            values = [entry.get() for entry in window.winfo_children() if isinstance(entry, tk.Entry)]
            cursor.execute("       ", values) # update sql function where values has player id
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "player deleted successfully!")
            window.destroy()

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    
    
####################################################################################################
# TEAM
    
    def add_team(self, window):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="W3124#azd!%",
                database="dbsproj"
            )
            cursor = conn.cursor()

            # Get values from entry widgets
            values = [entry.get() for entry in window.winfo_children() if isinstance(entry, tk.Entry)]

            # Insert data into the database
            cursor.execute("INSERT INTO teams (teamID, campusID, teamName, noOfPlayers, gender, sportID) VALUES (%s, %s, %s, %s, %s, %s)", values)
            conn.commit()

            # Close the connection
            conn.close()

            # Show success message
            messagebox.showinfo("Success", "Team added successfully!")

            # Close the window after successful insertion
            window.destroy()

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
                
    def del_team(self, window):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="W3124#azd!%",
                database="dbsproj"
            )
            cursor = conn.cursor()
            values = [entry.get() for entry in window.winfo_children() if isinstance(entry, tk.Entry)]
            cursor.execute("       ", values) # delete sql function where values has team id
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Team deleted successfully!")
            window.destroy()

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")  
    def update_team(self, window):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="W3124#azd!%",
                database="dbsproj"
            )
            cursor = conn.cursor()
            values = [entry.get() for entry in window.winfo_children() if isinstance(entry, tk.Entry)]
            cursor.execute("       ", values) # update sql function where values has team id
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Team updated successfully!")
            window.destroy()

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")        

####################################################################################################
#MATCH
    def add_match(self, window):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="W3124#azd!%",
                database="dbsproj"
            )
            cursor = conn.cursor()

            # Get values from entry widgets
            values = [entry.get() for entry in window.winfo_children() if isinstance(entry, tk.Entry)]

            # Insert data into the database
            cursor.execute("INSERT INTO match (match_id, team1_id, team2_id, venue, date, time, sport, ref_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", values)
            conn.commit()

            # Close the connection
            conn.close()

            # Show success message
            messagebox.showinfo("Success", "Match added successfully!")

            # Close the window after successful insertion
            window.destroy()

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def update_match(self, window):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="W3124#azd!%",
                database="dbsproj"
            )
            cursor = conn.cursor()
            values = [entry.get() for entry in window.winfo_children() if isinstance(entry, tk.Entry)]
            cursor.execute("       ", values) # update sql function where values has match id, teamwin
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "match updated successfully!")
            window.destroy()

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    
    def del_match(self, window):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="W3124#azd!%",
                database="dbsproj"
            )
            cursor = conn.cursor()
            values = [entry.get() for entry in window.winfo_children() if isinstance(entry, tk.Entry)]
            cursor.execute("       ", values) # delete sql function where values has match id
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "match deleted successfully!")
            window.destroy()

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")        
####################################################################################################
#referee
    def add_referee(self, window):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="W3124#azd!%",
                database="dbsproj"
            )
            cursor = conn.cursor()

            # Get values from entry widgets
            values = [entry.get() for entry in window.winfo_children() if isinstance(entry, tk.Entry)]

            # Insert data into the database
            cursor.execute("INSERT INTO referee (ref_id, sport, contact, remuneration) VALUES (%s, %s, %s, %s)", values)
            conn.commit()

            # Close the connection
            conn.close()

            # Show success message
            messagebox.showinfo("Success", "Referee added successfully!")

            # Close the window after successful insertion
            window.destroy()

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def update_ref(self, window):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="W3124#azd!%",
                database="dbsproj"
            )
            cursor = conn.cursor()
            values = [entry.get() for entry in window.winfo_children() if isinstance(entry, tk.Entry)]
            cursor.execute("       ", values) # update sql function where values has ref id, hours
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "ref updated successfully!")
            window.destroy()

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
        
    def gfors_window(self):
     window = tk.Toplevel(self)
     window.title("Gold for Sport")

     labels = ["Sport ID:"]
     self.create_labels_and_entries(window, labels, self.gfors)

    def gfors(self, window):
     try:
        print("Window children:", window.winfo_children())
        entries = [entry.get() for entry in window.winfo_children() if isinstance(entry, tk.Entry)]
        print("Entries:", entries)
        if entries:  # Check if entries list is not empty
            sport_id = entries[0]  # Get the first entry
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="W3124#azd!%",
                database="dbsproj"
            )
            cursor = conn.cursor()

            # Execute the SQL query with the provided sport ID
            cursor.execute("""
                SELECT s.sportName, t.teamName, MAX(w.noOfWins) AS wins 
                FROM sport s 
                INNER JOIN teams t ON s.sportID = t.sportID 
                INNER JOIN wins w ON t.teamID = w.teamID 
                WHERE s.sportID = %s 
                GROUP BY s.sportName, t.teamName 
                ORDER BY wins DESC 
                LIMIT 1;
            """, (sport_id,))

            # Fetch the results
            result = cursor.fetchone()
            
            # Close the connection
            conn.close()

            if result:
                # Display the results in a label
                result_label = tk.Label(window, text=f"Sport Name: {result[0]}\nTeam Name: {result[1]}\nWins: {result[2]}")
                result_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
            else:
                messagebox.showinfo("Info", "No data found for the provided sport ID.")

        else:
            messagebox.showerror("Error", "Please enter a sport ID.")

     except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")

     except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


    def mfors(self, window):
     try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="W3124#azd!%",
            database="dbsproj"
        )
        cursor = conn.cursor()

        # Get sport ID from entry widget
        sport_id = [entry.get() for entry in window.winfo_children() if isinstance(entry, tk.Entry)][0]

        # Execute SQL query with sport ID
        cursor.execute("SELECT s.sportName, t1.teamName AS team1, t2.teamName AS team2, m.date, m.time, m.venue FROM sport s, teams t1, teams t2, matches m WHERE s.sportID = %s AND m.sportID = %s AND m.team1ID = t1.teamID AND m.team2ID = t2.teamID;", (sport_id, sport_id))
        rows = cursor.fetchall()

        # Close the connection
        conn.close()

        # Display the results
        result_window = tk.Toplevel(window)
        result_window.title("Matches in Sport")
        result_label = tk.Label(result_window, text="Sport Name\tTeam 1\tTeam 2\tDate\tTime\tVenue")
        result_label.pack()
        for row in rows:
            result_label = tk.Label(result_window, text=f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}\t{row[5]}")
            result_label.pack()

     except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")

     except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

    def tinc(self, window):
     try:
        # Create a new window to get user input
        input_window = tk.Toplevel(window)
        input_window.title("Enter Campus ID")

        # Create a label and an entry for the user to input the campus ID
        label = tk.Label(input_window, text="Enter Campus ID:")
        label.pack()
        entry = tk.Entry(input_window)
        entry.pack()

        # Function to fetch data when the user clicks the button
        def fetch_data():
            campus_id = entry.get()
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="W3124#azd!%",
                database="dbsproj"
            )
            cursor = conn.cursor()

            # Execute SQL query with campus ID
            cursor.execute("SELECT c.campusName, t.teamID, t.teamName, s.sportName, t.gender FROM campus c, teams t, sport s WHERE c.campusID = %s AND t.campusID = %s AND t.sportID = s.sportID;", (campus_id, campus_id))
            rows = cursor.fetchall()

            # Close the connection
            conn.close()

            # Display the results
            result_window = tk.Toplevel(window)
            result_window.title("Teams in Campus")
            result_label = tk.Label(result_window, text="Campus Name\tTeam ID\tTeam Name\tSport Name\tGender")
            result_label.pack()
            for row in rows:
                result_label = tk.Label(result_window, text=f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}")
                result_label.pack()

            # Destroy the input window after fetching data
            input_window.destroy()

        # Create a button to trigger fetching data
        button = tk.Button(input_window, text="Fetch Data", command=fetch_data)
        button.pack()

     except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")

     except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


    def tins(self, window):
     try:
        print("Window children:", window.winfo_children())
        entries = [entry.get() for entry in window.winfo_children() if isinstance(entry, tk.Entry)]
        print("Entries:", entries)
        if entries:  # Check if entries list is not empty
            sport_id = entries[0]  # Get the first entry
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="W3124#azd!%",
                database="dbsproj"
            )
            cursor = conn.cursor()

            # Execute the SQL query with the provided sport ID
            cursor.execute("""
                SELECT t.teamID, s.sportName, t.teamName, c.campusName
                FROM teams t
                INNER JOIN campus c ON t.campusID = c.campusID
                INNER JOIN sport s ON t.sportID = s.sportID
                WHERE s.sportID = %s;
            """, (sport_id,))

            # Fetch all the results
            results = cursor.fetchall()
            
            # Close the connection
            conn.close()

            if results:
                # Display the results in a label
                result_label = tk.Label(window, text="Team ID\tSport Name\tTeam Name\tCampus Name")
                result_label.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
                
                for i, result in enumerate(results):
                    team_id, sport_name, team_name, campus_name = result
                    display_text = f"{team_id}\t{sport_name}\t{team_name}\t{campus_name}"
                    tk.Label(window, text=display_text).grid(row=i+1, column=0, columnspan=4, padx=10, pady=5)

            else:
                messagebox.showinfo("Info", "No data found for the provided sport ID.")

        else:
            messagebox.showerror("Error", "Please enter a sport ID.")

     except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")

     except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

if __name__ == "__main__":
    app = Application()
    app.mainloop()