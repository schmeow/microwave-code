import java.util.ArrayList;

public class Microwave
{
  private String string;
  private String encoded;
  private ArrayList<Integer> letters = new ArrayList<Integer>();
  private String[] Code;
  
  public Microwave(String s){
    string = s + "-00";
    encoded = "";
    Code = new String[]{"v.h.h", "v.h.m", "v.h.V", "v.h.M", "v.H.v", "v.H.h", "v.H.m", "v.H.V", "v.H.M", "h.h.v", "h.h.h", "h.h.m", "h.h.V", "h.h.M", "h.H.v", "h.H.h", "h.H.m", "h.H.V", "h.H.M", "m.h.v", "m.h.h", "m.h.m", "m.h.V", "m.h.M", "m.H.v", "m.H.h"};
    splitup();
    System.out.println(encode());
  }
  
  public void splitup(){
    String letter;
    int numberl;
    while (string.length() > 2)
    {
      if (string.length() > 2){
        letter = string.substring(0, string.indexOf("-"));
        string = string.substring(string.indexOf("-")+1, string.length());
        numberl = Integer.valueOf(letter);
        letters.add(numberl);
      }
    }
    letters.add(Integer.valueOf(string));
  }
 
  public String encode(){
    String enletter = "";
    for (int i = 0; i < letters.size()-1; i++){
      int let = letters.get(i);
      if (let == 0){
        encoded = encoded + "--";
      }
      else {
        enletter = Code[let - 1];
        if (encoded.equals("") || encoded.substring(encoded.length()-1).equals("-")) {
          encoded = encoded + enletter;
        }
        else
        {
          encoded = encoded + "-" + enletter;
        }
      }
    }
    return encoded;
  }
}