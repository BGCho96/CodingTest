## 1트 클  
나름 직관적이고 쉽고, 구현쪽에 바짝 붙은 문제였다.고 생각한다.  
행렬을 한땀한땀, 돌려주었다. 나름 차이?배운점? 이 있기는 했다.  
## 우리 왕뱀은요 그런거 안대요  
matlab 돌릴때는 rndstff[x1:x2][y1:y2] 이딴 깔쌈한 인덱싱이 가능했었는데....  
여기는 그런게 없다. 한땀한땀 픽셀(?) 단위로 반복문 돌려주는거 밖에 안되는거 같다...아마도...  
하여간 이런 편리한 인덱싱이 안되서 반복문 4줄로 4줄의 작업을 다 해줬다. 그래도 나름 직관적인 문제였는데도, 인덱스 변수 입력하는데 머가리 깨지는 줄 알았다.  
앞으론 앵간하면 패드나 a4 하나 들고 길이-1 이딴식으로 피곤한 인덱스 정리를 해주지 않으면... 타이트한 코테에서는 빡쎌 수 있겠다.  
그냥 한번씩 드는 방법중 하나는 해당 구역을 하나의 긴... 왕뱀(!) 처럼 만들어서 읽어들인 리스트를 밀고 당겨서 순서 바꾸는.... 상상을 해봤다.  
이런 방법은 뭐가 필요할까? 한 10초 생각해보니까 어려워보이지는 않는다.  
1. 관심구역을 하나씩 따와서 리스트에 어펜드.  
2. 방향에 맞게 pop, append 때리거나, 잘라서 붙여도 되겠지. 하여간 편집.  
3. 그러고 나서 구역 따온 for문에 대응하는 동일 구간에 하나씩 pop 해서 넣기.  
이 방법을 쓰면 n 칸 밀기, 특히 n이 입력값보다 클 때에 아주 효과적으로 사용 할 수 있겠지. 솔직히 input의 크기를 고려하지 않아도 되는 이유중 하나는 한칸만 움직이기에 가능했던 거다.  
좀 더 다양한 변수로 좀 더 다양한 method들을 풀어줬다면 골아팠을지도....  
어쩃든 한번에 풀렸으면서도, 내가 죽쓰는 구현 파트이면서도, 무엇보다 programmers에서 완료한 사람 수가 적은 문제를 비교적 수월하게 풀어서 기부니가 기모찌했다.
