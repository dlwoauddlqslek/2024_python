'''
    csv파일 다루기
    파일: 인천광역시_부평구_인구현황.csv
    [조건1] 부평구의 동 마다 Region 객체 생성해서 리스트 담기
    [조건2]
        Region 객체 변수:
        1. 동이름 2. 총인구수 3. 남인구수 4.여인구수 5.세대수
        Region 함수
            남자 비율 계산
            여자 비율 계산
    [조건3] 모든 객체의 정보를 f포매팅 해서 console 창에 출력하시오
    [조건4] 출력시 동 마다 남여 비율 계산해서 출력하시오.
    출력예시
'''
from region import Region
def read():
    f=open('인천광역시_부평구_인구현황.csv','r')
    lines=f.read()
    info=lines.split('\n')
    regions=[]
    for line in info[:len(info)-1]:
        if line:
            # Region.percent1(line.split(',')[1], line.split(',')[2])
            region=Region(line.split(',')[0],line.split(',')[1],line.split(',')[2],line.split(',')[3],line.split(',')[4])
            region.percent1( )
            regions.append(region)
    for people in regions:
        print(f'{people.name:5}  {people.total:>5}  {people.male:>5}  {people.female:>5}  {people.group:>5} { people.percent1() }')




if __name__=="__main__":
    print('--start--')
    read()