import java.util.Scanner;

// Creating Project class and class attributes
public class Project {
	String projectNumber;
	String projectName;
	String buildingType;
	String address;
	String erfNumber;
	int projectFee;
	int amountPaid;
	String dueDate;
	Person architect;
	Person contractor;
	Person customer;
	boolean finalized = false; // Boolean to change project status
	
	//Creating constructor
	public Project(String projectNumber,String projectName, String buildingType, 
			String address, String erfNumber, int projectFee,
			int amountPaid, String dueDate,Person architect, Person customer,Person contractor) {
		this.projectNumber = projectNumber;
		this.projectName = projectName; 
		this.buildingType = buildingType;
		this.address = address;
		this.erfNumber = erfNumber;
		this.projectFee = projectFee;
		this.dueDate = dueDate;
		this.amountPaid = amountPaid;
		this.contractor = contractor;
		this.finalized = finalized;
	//Creating class getters and setters 
	}
	public int getProjectFee() {
		return this.projectFee;
	}
	public int getAmountPaid() {
		return this.amountPaid;
	}
	public String getDueDate() {
		return this.dueDate;
	}
	//Creating a class method to calculate the project balance
	public int ProjectBalance() {
		return this.projectFee - this.amountPaid;
	}
	//Creating a class method to change the project status
	public boolean changeProjectStatus() {
		return this.finalized = true;
	}
//Creating methods to change the due date
public void changeDuedate() {
	Scanner scanner = new Scanner(System.in);
	System.out.println("Enter new due date (format dd mon yyyy: ");
	this.dueDate = scanner.next();
		
	}
//Creating method to update the amount paid for the project
public void amountChange() {
	Scanner scanner = new Scanner(System.in);
	System.out.println("What is the updated total amount paid for the project ");
	this.amountPaid  = scanner.nextInt();
	
}
//Creating a method to change the contractors contact details
public void detailsChange() {
	Scanner scanner = new Scanner(System.in);
	System.out.println("What is the contractors new phone number?:");
	String newPhonenumber = scanner.next();
	contractor.setPhoneNumber(newPhonenumber);
		
}

//Creating a method to print an invoice
public String toString() {
	String output = "Invoice: ";
	output += "Name: " + customer.getName();
	output += "\nNumber:" + customer.getPhoneNumber();
    output += "\nCompletion date:" + getDueDate();
    output += "\nBalance:" + ProjectBalance();
    return output;
}
//Creating a project list will contain a list of project objects
Project [] projectlist;{

//Creating a for loop to loop through the project list and print invoices for projects that are not finalized
for (int i=0; i < projectlist.length; i++) {
	if(projectlist[i].ProjectBalance() > 0) {
		toString();
	}
	else {
		changeProjectStatus(); //Else changes project status to finalized
	}


}
	
}
}







