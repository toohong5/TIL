# Bootstrap

- html 과 margin 값이 다름.
- html 보다 깔끔함
- bootstrap 홈페이지->documentaion-> quick start -> css 복사 -> head의 하단에 -> js는 body의 하단에...

- CDN : Content Delivery Network, 여러 노드에 가진 네트워크에 데이터를 제공하는 시스템, 메모리 덜 사용함, 한번 들어갈때 저장됨.

## 1.1 spacing

- .m-0; => margin: 0
- .mr-0; => margin-right: 0
- .py-0 => padding-top: 0; padding bottom: 0;
- .mt-1
- .mt-2 => 8px
- .mt-3 =>
- .mx-auto => 가운데 정렬



## 1.2 color

- primary => .bg-primary로 사용
- secondary
- success
- info
- warning
- 색바꾸기
  - .text-success
  - .alert-warning
  - .btn-secondary => 

## 1.3 border

- .border : 4 방향
- .border.border-색상



## 1.4 display

- display: block=> .d-block, .d-inline, .d-none



## 1.5 position

- .position-static
- .fixed-top, .fixed-bottom

## 1.6 text

- text-align:center => .text-center
- font-weight: bold => .font-weight-bold



## 1.7 css layout history

1. 레이아웃이 없던 시절
2. 테이블 레이아웃
3. 프레임 레이아웃
4. CSS(float/position)
5. flex box
6. grid system

- grid는 flex box를 완전 대체하지는 못한다. 큰 틀을 grid로 짜고 세부사항을 flex box로 사용한다!!