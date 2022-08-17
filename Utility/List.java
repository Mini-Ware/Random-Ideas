import java.util.HashMap;
import java.util.Scanner;

/*
class Item{
	String title;
	boolean completed;

	Item(String x, boolean y){
		this.title = x;
		this.completed = y;
	}

	public void finished(boolean status){
		this.completed = status;
	}

	public String getName(){
		return this.title;
	}
}*/

public class List{
	public static void main(String[] args){
		//Initialise variables
		boolean leaving = true;
		HashMap<String, Boolean> tasks = new HashMap<String, Boolean>();

		//Objects and functions
		Scanner ask = new Scanner(System.in);

		//Main loop
		while (leaving){
			//Show options
			System.out.println("1) Create item");
			System.out.println("2) Read items");
			System.out.println("3) Update item");
			System.out.println("4) Delete item");
			System.out.println("q) Quit");

			//Gather input
			System.out.print("Enter option: ");
			String option = ask.nextLine();
			switch (option){
				//Create
				case "1":
					System.out.print("Name of item: ");
					String name = ask.nextLine();
					tasks.put(name, false);
					System.out.println("Item created!");
					break;
				//Read
				case "2":
					for (String i : tasks.keySet()){
						if (tasks.get(i)){
							System.out.println("+ "+i);
						}else{
							System.out.println("- "+i);
						}
					}
					break;
				//Update
				case "3":
					System.out.print("Complated item: ");
					String target = ask.nextLine();
					tasks.put(target, true);
					System.out.println("Item updated!");
					break;
				//Delete
				case "4":
					System.out.print("Target item: ");
					String trash = ask.nextLine();
					tasks.remove(trash);
					System.out.println("Item deleted!");
					break;
				//Quit
				case "q":
					System.exit(0);
					break;
			}
		}
		ask.close();
	}
}
