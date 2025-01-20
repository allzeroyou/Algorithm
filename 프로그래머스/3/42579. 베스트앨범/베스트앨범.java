import java.util.*;

class Solution {
    public int[] solution(String[] genres, int[] plays) {
        
        int[] answer = {};
        
        // 1. HashMap 생성
        HashMap<String, List<int[]>> genMap = new HashMap<>();
        
        for(int i=0; i<genres.length; i++){
            // 장르가 없으면 새 리스트 추가
            genMap.putIfAbsent(genres[i], new ArrayList<>() ); 
            genMap.get(genres[i]).add(new int[]{plays[i], i}); // [재생수, 인덱스 저장]
        }
        
        // 2. 기준 1: 가장 많이 재생된 장르 찾기
        // 장르별 재생수 합을 기준으로 정렬
        ArrayList<String> sortedGen = new ArrayList<>(genMap.keySet());
        
        sortedGen.sort((g1, g2)->{
            int total1 = genMap.get(g1).stream().mapToInt(arr->arr[0]).sum();
            int total2 = genMap.get(g2).stream().mapToInt(arr->arr[0]).sum();
            return Integer.compare(total2, total1); // 내림차순 정렬
        });
        
        // 3. 기준 2: 장르내 가장 많이 재생된 노래
        List<Integer> result = new ArrayList<>();
        
        for(String genre: sortedGen){
            List<int[]> song= genMap.get(genre);
            
            song.sort((s1, s2)->{
                if(s1[0]==s2[0]){ // 재생수 같다면 고유번호 오름차순 정렬
                    return Integer.compare(s1[1], s2[1]);
                }
                return Integer.compare(s2[0], s1[0]); // 재생수 기준 내림차순
            });
            
            // 상위 2곡만 선정(but, 2곡이 없을 경우: 곡 수, 2-> 둘 중 최솟값으로)
            for(int i=0; i< Math.min(song.size(), 2); i++){
                result.add(song.get(i)[1]); // 인덱스 추가
            }
        }
        
        // 결과 -> 배열로 변환
        answer = result.stream().mapToInt(i->i).toArray();
        
        return answer;
    }
}