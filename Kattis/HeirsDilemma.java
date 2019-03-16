import java.util.*;

public class HeirsDilemma{
	public static void main(String[] args) {
		Scanner kb = new Scanner(System.in);
		String ins = kb.nextLine();
		String[] l = ins.split(" ");
		int c = 0;
		for (int i = Integer.parseInt(l[0]); i <= Integer.parseInt(l[1]); i++) 
			if (comb(i))
				c++;
		System.out.println(c);
	}
	public static boolean comb(int n) {
		int[] l = new int[6];
		int cp = n;
		int c = 1;
		while (cp > 0) {
			l[6 - c] = cp % 10;
			c++;
			cp = cp / 10;
		}
		for (int i = 0; i < l.length; i++) {
			if (l[i] == 0)
				return false;
			for (int y = i + 1; y < l.length; y++)
				if (l[i] == l[y])
					return false;
		}
		for (int i = 0; i < l.length; i++)
			if (n % l[i] != 0)
				return false;
		return true;
	}
}