class Solution {
public:
    int atoi(const char *str) {
        bool isNeg = false;
        unsigned long long ret = 0;

        // skip leading white spaces
        while(*str==' ') str++;

        // first none white space char must be +- or digit
        if(!isdigit(*str) && *str!='+' && *str!='-') return 0;

        // for +-, next char must be digit
        if(*str=='+' || *str=='-') {
            if(!isdigit(*(str+1))) return 0;
            if(*str=='-') isNeg = true;
            str++;
        }

        while(isdigit(*str)) {
            ret = ret*10 + (*str - '0');
            if(ret>(unsigned long long)INT_MAX)
                return isNeg ? INT_MIN : INT_MAX;
            str++;
        }
        return isNeg ? -(int)ret : (int) ret;
    }
};
