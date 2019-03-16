import java.util.*;
public class Ptice{
	public static void main(String[] args) {
		Scanner kb = new Scanner(System.in);
		int questions = kb.nextInt();
		kb.nextLine();
		String corr = kb.nextLine();
		String[] adrian = {"A","B","C"};
		int aR = 0;
		String[] bruno = {"B", "A", "B", "C"};
		int bR = 0;
		String[] goran = {"C", "C","A", "A", "B", "B"};
		int gR = 0;
		ArrayList<String> input= new ArrayList<String>();
		for(int i = 0;i<questions;i++)
			input.add(corr.substring(i,i+1));
		int bPos = 0;
		int aPos = 0;
		int gPos = 0;
		for(String x:input) {
			if(bPos==4) 
				bPos = 0;
			if(aPos==3) 
				aPos = 0;
			if(gPos==6) 
				gPos = 0;
			if(adrian[aPos].equals(x)) 
				aR++;
			if(bruno[bPos].equals(x)) 
				bR++;
			if(goran[gPos].equals(x)) 
				gR++;
			bPos++;
			aPos++;
			gPos++;
		}
		if(aR>bR && aR>gR) {
			System.out.println(aR);
			System.out.println("Adrian");
		}
		else if(bR>aR && bR>gR) {
			System.out.println(bR);
			System.out.println("Bruno");
		}
		else if(gR>bR && gR>aR) {
			System.out.println(gR);
			System.out.println("Goran");
		}
		else if(gR==aR && gR==bR){
			System.out.println(gR);
			System.out.println("Adrian");
			System.out.println("Bruno");
			System.out.println("Goran");
		}
		else if(gR==aR) {
			System.out.println(gR);
			System.out.println("Adrian");
			System.out.println("Goran");
		}
		else if(gR==bR) {
			System.out.println(gR);
			System.out.println("Bruno");
			System.out.println("Goran");
		}
		else if(aR==bR) {
			System.out.println(aR);
			System.out.println("Adrian");
			System.out.println("Bruno");
		}
	}
}