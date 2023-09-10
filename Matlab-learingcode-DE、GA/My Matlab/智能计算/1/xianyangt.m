function xianyangt
%320085404113
clc;
clear;
n=50;                                           %种群数量
w=8;                                            %变量维数
up=50;ul=-50;                                     %变量上限下限
p=(up-ul)*rand(n,w)+ul;                         %生成初始种群
yj=pj(p);   pjc=n;                              %对初始种群评价 初始评价次数
[yj,d]=sort(yj);                                %评价值排序
p=p(d,:);                                       %对种群排序
xl0=0;                                          %初始化代数
while xl0<40000 %迭代次数定为5000
    v0=[];%生成空矩阵
    
    for i=1:n
         r=randperm(10);r1=r(1);
         r=randperm(n-r1)+r1;r2=r(1);r3=r(2);
         if r2>r3,x=r2;r2=r3;r3=x;end %生成r1r2r3
         v=p(r1,:)+0.4*rand(1,w).*(p(r2,:)-p(r3,:)); %生成一个差分矢量
         x=(up-ul)*rand(1,w)+ul;%生成一个新的个体x
         
         x0=v>up|v<ul;%判断v的元素是否越界，返回1行5列的逻辑数组
         x1=any(x0);%判断x0的每一列是否为非零元素 返回0或者1
         if rand<0.8||x1%满足此条件就替换 rand<0.8或者x1为1
             x2=rand(1,w)<0.2;%产生一个逻辑数组x2
             x3=fix(rand*w)+1;%生成x3（1-5之间）
             x0(x3)=true;
             x4=x0|x2;
             v(x4)=x(x4);%替换越界的那个数
         end
         v0=[v0;v];%把v放入v0中
     end
          pjx=pj(v0);  %对新种群v0评价
          pjc=pjc+n;   %计算评价次数                      
         pp=[p;v0]; %把新旧种群放在一起
         ppj=[yj;pjx]; %把评价值放在一起                        
         [yj,d]=sort(ppj);%评价值排序
         p=pp(d(1:n),:);  %取前30个个体
       
         yj=yj(1:n); %取前30个解 
         [p([1:5],:),yj(1:5)];%显示出前5个个体
          if yj(1)<1e-5,break,end %精度小于1e-5，则停止
         xl0=xl0+1;%代数+1
         if xl0==1
          figure(1)
         axis([-50,50,-50,50]),plot(p(:,1),p(:,2),'*') 
         end
          if xl0==100
          figure(2)
         axis([-50,50,-50,50]),plot(p(:,1),p(:,2),'*') 
         end
end
%%
disp(['bestfi:   ',num2str(p(1,:))])       %显示最好的个体
disp(['bests:    ',num2str(yj(1))])         %显示最好的解
pjc; xl0                                          %评价次数
figure(3)
axis([-50,50,-50,50]),plot(p(:,1),p(:,2),'*') 
end

%% 函数
function y=pj(x)                                                   
y=sum(x.^2,2);
end
