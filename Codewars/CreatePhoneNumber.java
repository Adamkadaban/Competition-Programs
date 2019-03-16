import java.util.ArrayList;
public class Kata {
  public static String createPhoneNumber(int[] numbers) {
    ArrayList x = new ArrayList();
    for(int i=0;i<numbers.length;i++)
      x.add(numbers[i]);
    x.add(0,"(");
    x.add(4,") ");
    x.add(8,"-");
    String s="";
    for(int i=0;i<x.size();i++)
      s+=x.get(i);
    return s;
  }
}