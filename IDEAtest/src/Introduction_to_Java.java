/**
 * @author Hierarch
 */
public class Introduction_to_Java {
    public static void main(String[] args) {
        Person_1 per = new Person_1();
        per.name = "肖战";
        per.age = 80;
        per.showName();
        System.out.println(per.getAge());
        per.eat("shit");
        per.moveType = "爪巴";
        System.out.println(per.move());
    }
}
