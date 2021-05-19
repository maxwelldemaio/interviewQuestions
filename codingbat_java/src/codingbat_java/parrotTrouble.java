/**
 * 
 */
package codingbat_java;

/**
 * @author maxde
 *We have a loud talking parrot. The "hour" parameter 
 *is the current hour time in the range 0..23. 
 *We are in trouble if the parrot is talking and the hour 
 *is before 7 or after 20. Return true if we are in trouble.

parrotTrouble(true, 6)  true
parrotTrouble(true, 7)  false
parrotTrouble(false, 6)  false
*/

public class parrotTrouble {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println(code(false, 2));
		System.out.println(code(true, 4));
		System.out.println(code(true, 5));
	}
	
	public static boolean code(boolean talking, int hour) {
		  if (!talking) {
			  return false;
		  } else if (talking && (hour < 7 || hour > 20)) {
			  return true;
		  } else {
			  return false;
		  }
	}
	
}
