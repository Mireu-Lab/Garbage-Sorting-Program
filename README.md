# Garbage Sorting Program

## 개요

쓰래기 분류 알고리즘을 이용하여 쓰래기의 분류작업을 더 손쉽게 할수있게 도와주는 분류 AI입니다.

해당 프로그램은 쓰래기 분류 프로그램을 개발하기위해서 만들어진 레포입니다.

해당 프로그램의 데이터셋은 [여기](https://www.kaggle.com/asdasdasasdas/garbage-classification)을 클릭하시면 들어가실수있습니다.


## API 

```shell
curl -i -X POST \
    -H "Content-Type:image/jpeg" \
    -T "{file_location}.{file_type}" \
    'http://9aea11c286.mireu.xyz/app'
```

동작 결과시 아래와 같이 실행이됩니다

```json
{
	"trash" : 1
}
```

 

`{"trash":1}` 앞 내용은 쓰래기 결과이며 뒤에있는 숫자는 정확도을 출력하게 됩니다

해당 API는 금속, 유리, 종이, 일반쓰래기, 박스, 플라스틱을 분류하실 수 있습니다.