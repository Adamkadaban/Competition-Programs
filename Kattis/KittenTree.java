import java.util.*;

public class KittenTree {
    public static void main(String[] args) {
        Scanner kb = new Scanner(System.in);
        int x = kb.nextInt();
        String found = " "+x+" ";
        kb.nextLine();
        ArrayList<String> tree = new ArrayList<String>();
        boolean r = true;
        while(r) {
            String s = kb.nextLine();
            if(s.equals("-1"))
                r = false;
            else 
                tree.add(" "+s+" ");
        }
        System.out.print(x+" ");
        boolean r2 = true;
        while(r2) {
            int pos = getFirst(found,tree);
            if(pos==-1) 
                r2 = false;
            else {
                x = getNums(pos,tree);
                System.out.print(x+" ");
                found = " "+x+" ";
            }
        }
    }
    public static int getFirst(String find,ArrayList<String> tree) {
        for(int x = 0;x<tree.size();x++) 
            if(tree.get(x).indexOf(find)>1) 
                return x;
        return -1;
    }
    public static int getNums(int position, ArrayList<String> tree){
        String[] split = tree.get(position).split(" ");
        return Integer.parseInt(split[1]);
    }
}
