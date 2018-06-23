class Solution {
    
private:
    bool isVowel(char c) {
        char vowels[] = {'a','e','i','o','u','A','E','I','O','U'};
        for(int i = 0; i<= 9; i++){
            if(c == vowels[i])
                return true;
        }
        return false;
    }
    
    void swap(string& s, int i, int j) {
        char temp = s[i];
        s[i] = s[j];
        s[j] = temp;
    }
    
public:
    string reverseVowels(string s) {
        //2-pointer method, swap if vowels
        int i = 0;
        int j = s.length() -1;
        while(i < j)
        {
            if(this->isVowel(s[i]) && this->isVowel(s[j])){
                this->swap(s, i, j);
            }
            
            else if(this->isVowel(s[i])) {
                j--;
                continue;
            }
            
            else if(this->isVowel(s[j])) {
                i++;
                continue;
            }
            
            i++;
            j--;
        }
        return s;
    }
};
