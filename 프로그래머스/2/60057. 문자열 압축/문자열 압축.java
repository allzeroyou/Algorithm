class Solution {
    public int solution(String s) {
        int answer = s.length();
        
        int HALF = s.length()/2;
        
        for(int i=1; i<=HALF; i++) {
        	String slice = s.substring(0, i);
        	
        	String compare_str = compare(i, s, slice);
        	
        	answer = Math.min(answer, compare_str.length());
        }
        
        return answer;
    }
    
    public String compare(int len, String s, String slice) {
    	
    	String result = "";
    	int count = 1;
 
       	for(int i=len; i<s.length(); i+=len) {
       		int limit = i+len;
       		if(i+len >= s.length()) {
       			limit = s.length();
       		}
    		String target = s.substring(i, limit);
    		if(slice.equals(target)) {
    			count++;
    		}
    		else {
    			if(count == 1) {
    				result += slice;
    			}
    			else {
    				result += (count + slice);
    			}
    			count = 1;
    			slice = target;
    		}
    	}
    	
    	if(count == 1) {
    		result += slice;
    	}
    	else {
    		result += (count + slice);
    	}
 
    	return result;
    }
}