function mga1
clc;clear
%% 参数设置
n=100;                                           %种群个数
w=10;                                            %维数
up=5;ul=-5;                                     %变量上下限
p=(up-ul)*rand(n,w)+ul;                         %种群初始化
yj=pj(p);                                       %对初始种群评价
[yj,d]=sort(yj);                                %评价值排序
p=p(d,:);                                       %对种群排序
%axis([-5,5,-5,5]),plot(p(:,1),p(:,2),'*')       %绘出初始种群分布
xl=1000;                                         %迭代次数
xl0=1;                                          %初始化代数
%% 
by=0.05;                                        %变异概率
while xl0<xl
    xl0=xl0+1;                                  %代数+1
%% 交叉
    for i=1:n                                   %遍历每个个体
    n1=fix(rand*10)+1;                          %随机选一个个体
    n2=fix(rand*(n-n1))+n1;                     %再随机选一个个体
    alf=rand;                                   %产生一个随机数
    px(i,:)=alf*p(n1,:)+(1-alf)*p(n2,:);        %产生一个新个体
%% 变异
        if rand<by
            m0=rand(1,w)<0.1;                   %产生1行5列的随机数，判断是否小于变异概率，返回一个逻辑数组
            sw=fix(rand*w)+1;                   %在1-5中随机选取一个位置
            m0(sw)=true;                        %如果选取的位置在m0中是1（True）
            m1=(up-ul)*rand(1,w)+ul;            %
            m2=px(i,:);m2(sw)=m1(sw);px(i,:)=m2;
        end
    end
    pjx=pj(px);                                 %对新种群进行评价
    pp=[p;px];                                  %初始种群和新种群放在一起
    ppj=[yj;pjx];                               %初始种群和新种群的评价值放在一起
   % plot(pp(:,1),pp(:,2),'d'),axis([-5,5,-5,5]) %
    [yj,d]=sort(ppj);                            %放在一起后排序（升序
    p=pp(d(1:n),:);                             %种群取前30个
    yj=yj(1:n);                                 %评价值取前30个
   % [p(1:10,:),yj(1:10)]                        %显示前10个个体及其评价值

end
xl0
bestfi=[p(1,:)]
bests=[yj(1)]
function y=pj(x)
y=sum(x.^2,2);
end
end
