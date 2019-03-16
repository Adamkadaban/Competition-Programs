import java.util.Scanner;
import java.util.ArrayList;

public class Apaxiaaaaaaaaaaaans{
	public static String shortenName(String str) {
		ArrayList<String> a = new ArrayList<String>();
		for(int i=0;i<str.length();i++)
			a.add(str.substring(i,i+1));
		String temp="";
		for(int i=0;i<a.size();i++) {
			temp=a.get(i);
			int t=i+1;
			while(t<a.size()&&a.get(t).equals(temp))
				t++;
			if(t>i+1) {
				for(int j=t-1;j>i;j--)
					a.remove(j);
			}
		}
		String r ="";
		for(int i=0;i<a.size();i++)
			r=r+a.get(i);
		return r;
	}
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println(shortenName(sc.nextLine()));
	}
}