% Optimizing a function  using Simple Genetic Algorithm with elitist preserved

%Max f(x1,x2)=100*(x1*x1-x2).^2+(1-x1).^2; -2.0480<=x1,x2<=2.0480


%下面为代码。函数最大值为3904.9262，此时两个参数均为-2.0480，有时会出现局部极值，此时一个参数为-2.0480，一个为2.0480。变
%异概率pm=0.05，交叉概率pc=0.8。

clc;clear all;

format long;%设定数据显示格式

%初始化参数

T=1000;%仿真代数

N=200;% 群体规模

pm=0.05;pc=0.8;%交叉变异概率

umax=30;umin=-30;%参数取值范围

L=10;%单个参数字串长度，总编码长度Dim*L
Dim=10;%Dim维空间搜索

bval=round(rand(N,Dim*L));%初始种群，round函数为四舍五入

bestv=-inf;%最优适应度初值
funlabel=2;       %选择待优化的函数，1为Rastrigin,2为Schaffer,3为Griewank
% Drawfunc(funlabel);%画出待优化的函数，只画出二维情况作为可视化输出

%迭代开始

for ii=1:T

%解码，计算适应度

    for i=1:N  %对每一代的第i个粒子
        for k=1:Dim
            y(k)=0;
            for j=1:1:L  %从1到L，每次加以1

               y(k)=y(k)+bval(i,k*L-j+1)*2^(j-1);%把第i个粒子转化为十进制的值，例如y1是第一维

            end 
            x(k)=(umax-umin)*y(k)/(2^L-1)+umin;%转化为实际的x1
        end

  %     obj(i)=100*(x1*x1-x2).^2+(1-x1).^2; %目标函数 
       obj(i)=fun(x,funlabel);
       xx(i,:)=x;

    end

    func=obj;%目标函数转换为适应度函数

    p=func./sum(func);

    q=cumsum(p);%累加

    [fmax,indmax]=max(func);%求当代最佳个体

   if fmax>=bestv

      bestv=fmax;%到目前为止最优适应度值

      bvalxx=bval(indmax,:);%到目前为止最佳位串

      optxx=xx(indmax,:);%到目前为止最优参数

   end   

   Bfit1(ii)=bestv; % 存储每代的最优适应度

%%%%遗传操作开始

%轮盘赌选择

 for i=1:(N-1)

    r=rand;

    tmp=find(r<=q);

    newbval(i,:)=bval(tmp(1),:);

 end

  newbval(N,:)=bvalxx;%最优保留

  bval=newbval;

%单点交叉

    for i=1:2:(N-1)

       cc=rand;

       if cc<pc

           point=ceil(rand*(2*L-1));%取得一个1到2L-1的整数

           ch=bval(i,:);

           bval(i,point+1:2*L)=bval(i+1,point+1:2*L);

           bval(i+1,point+1:2*L)=ch(1,point+1:2*L);

        end

    end   

    bval(N,:)=bvalxx;%最优保留

    %位点变异

    mm=rand(N,Dim*L)<pm;%N行

    mm(N,:)=zeros(1,Dim*L);%最后一行是精英不变异，强制赋0

    bval(mm)=1-bval(mm); 

end

%输出
  figure;
% 
 plot(-Bfit1);% 绘制最优适应度进化曲线

bestv   %输出最优适应度值

optxx    %输出最优参数

