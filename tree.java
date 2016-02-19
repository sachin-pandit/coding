
class Treenode {
        int val;
        Treenode left;
        Treenode right;

        Treenode (int num) {
                this.val = num;
        }
}

public class tree {
        static int nextH = 0;

        static int print_next_highest (Treenode head, int num) {
                if (head == null) {
                        return nextH;
                } else if (head.val == num) {
                        return head.val;
                } else if (head.val > num) {
                        if (head.val < nextH || nextH == -1)
                                nextH = head.val;
                        nextH = print_next_highest (head.left, num);
                } else if (head.val < num) {
                        nextH = print_next_highest (head.right, num);
                }
                return nextH;
        }

        static void inorder (Treenode head) {
                if (head == null)
                        return;
                inorder (head.left);
                System.out.print (head.val + " ");
                inorder (head.right);
        }

        public static void main (String[] str) {
                Treenode head = new Treenode(10);
                head.left = new Treenode (5);
                head.left.left = new Treenode (3);
                head.left.right = new Treenode (7);
                head.left.right.left = new Treenode (6);
                head.left.right.right = new Treenode (8);
                head.left.left.left = new Treenode (1);
                head.right = new Treenode (12);
                head.right.right = new Treenode (13);
                inorder (head);
                System.out.println();
                nextH = -1;
                System.out.println (print_next_highest (head, 1000));
        }
}
