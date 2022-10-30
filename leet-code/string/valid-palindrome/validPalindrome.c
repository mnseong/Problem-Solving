#include <stdio.h>
#include <string.h>
#include <ctype.h>
typedef enum { false, true } bool;

// Using Two Pointers
bool isPalindrome(char* s) {
    int biasLeft = 0;
    int biasRight = 1;
    int length = strlen(s);
    for (int i = 0; i < length; i++) {
        while (!isalnum(s[i+biasLeft])) {
            biasLeft++; // 문자나 숫자가 아니면 skip
            if (i+biasLeft == length)
                return true;
        }
        while (!isalnum(s[length-i-biasRight])) {
            biasRight++;
        }
        if (i+biasLeft >= length-i-biasRight)
            break;
        if (tolower(s[i+biasLeft]) != tolower(s[length-i-biasRight]))
            return false;
    }
    return true;
}

int main() {
    bool result;
    char* testcase1 = "A man, a plan, a canal: Panama";
    char* testcase2 = "race a car";
    char* testcase3 = "";
    printf("%d %d %d\n", isPalindrome(testcase1), isPalindrome(testcase2), isPalindrome(testcase3));
    return 0;
}