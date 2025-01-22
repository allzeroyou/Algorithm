class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = new int[2];
        
        int mid = brown/2;
        
        int flag = 0;
        
        for(int i=mid; i>0; i--){
         
            for(int j=mid-1; j>0; j--){
                if((i-2)*(j-2)==yellow && (i*2)+(j-2)*2==brown ) {
                    answer[0]=i;
                    answer[1]=j;
                    flag= 1;
                    break;
                }
            }
               if(flag==1){
                break;
            }
        }
        
        return answer;
    }
}