//Creating person class
public class Person {
	String name;
	String phoneNumber;
	String emailAddress;
	String address;
	
	//Creating class constructor
	public Person(String name, String phoneNumber, String emailAddress, String address) {
	this.name = name;
	this.phoneNumber = phoneNumber;
	this.emailAddress = emailAddress;
	this.address = address;
	
	}
	//Creating class getters and setters
	public String getName() {
		return this.name;
	}
	public String getPhoneNumber() {
		return this.phoneNumber;
		
	}
		
	public String getEmail() {
		return this.emailAddress;
	}
	public String getAddress() {
		return this.address;
	}
	public void setName(String newName) {
		this.name = newName;
		
	}
	public void setPhoneNumber(String newPhonenumber) {
		this.phoneNumber = newPhonenumber;
	}
	public void setEmail(String newEmail) {
		this.emailAddress = newEmail;
	}
	public void setAddress(String newAddress) {
		this.address = newAddress;
	}
}