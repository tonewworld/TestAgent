/**
 * 工具类 —— 被测试程序（Java 版）
 * 包含：计算器、字符串校验、简单栈
 */
package sample;

public class Utils {

    // ==================== Calculator ====================

    public static class Calculator {
        public static int add(int a, int b) { return a + b; }
        public static int subtract(int a, int b) { return a - b; }
        public static int multiply(int a, int b) { return a * b; }

        public static double divide(double a, double b) {
            if (b == 0) throw new IllegalArgumentException("除数不能为零");
            return a / b;
        }

        public static double power(double base, int exp) {
            if (exp < 0) throw new IllegalArgumentException("暂不支持负指数");
            return Math.pow(base, exp);
        }
    }

    // ==================== StringValidator ====================

    public static class StringValidator {
        public static boolean isValidEmail(String email) {
            if (email == null || !email.contains("@")) return false;
            String[] parts = email.split("@", 2);
            if (parts.length != 2 || parts[0].isEmpty() || parts[1].isEmpty()) return false;
            return parts[1].contains(".");
        }

        public static boolean isValidPhone(String phone) {
            if (phone == null || phone.length() != 11) return false;
            return phone.startsWith("1") && phone.matches("\\d+");
        }

        public static int passwordStrength(String pwd) {
            if (pwd == null || pwd.length() < 6) return 0;
            boolean hasDigit = pwd.matches(".*\\d.*");
            boolean hasAlpha = pwd.matches(".*[a-zA-Z].*");
            boolean hasSpecial = pwd.matches(".*[^a-zA-Z0-9].*");
            if (pwd.length() >= 8 && hasDigit && hasAlpha && hasSpecial) return 2;
            if (hasDigit && hasAlpha) return 1;
            return 0;
        }

        public static String truncate(String text, int maxLen) {
            if (text == null) return "";
            if (maxLen <= 0) throw new IllegalArgumentException("maxLen 必须大于0");
            if (text.length() <= maxLen) return text;
            return text.substring(0, maxLen) + "...";
        }
    }

    // ==================== Stack ====================

    public static class Stack<T> {
        private java.util.ArrayList<T> items = new java.util.ArrayList<>();

        public void push(T item) { items.add(item); }

        public T pop() {
            if (isEmpty()) throw new IndexOutOfBoundsException("栈为空");
            return items.remove(items.size() - 1);
        }

        public T peek() {
            if (isEmpty()) throw new IndexOutOfBoundsException("栈为空");
            return items.get(items.size() - 1);
        }

        public boolean isEmpty() { return items.isEmpty(); }
        public int size() { return items.size(); }
    }
}
