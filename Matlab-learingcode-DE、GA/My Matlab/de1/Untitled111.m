close all;
clear all;
clc;
NP=50;
D=10;        % 染色体长度
G=1000;
F0=0.4;
CR=0.1;
a=-20;     % 寻优区间
b=20;
yz=10^-5;
 
x=zeros(NP,D);    % 初始种群
v=zeros(NP,D);    % 变异种群
u=zeros(NP,D);    % 选择种群
%   种群怫初值
x=rand(NP,D)*(b-a)+a;
%   计算目标参数
for i=1:1:NP
    ob(i)=sum(x(i,:).^2);  
end
% pjz=[];
% for i=1:size(population,1)
%    x=population(i,:);
%    pj=Rastrigin(x);
%    pjz=[pjz;pj];
% end
trace(1)=min(ob);
%          差分进化循环
for gen=1:G
    %   变异操作
    for m=1:NP
        r1=randi([1,NP],1,1);
        while(r1==m)
            r1=randi([1,NP],1,1);
        end
        
        r2=randi([1,NP],1,1);
        while(r2==r1)||(r2==m)
            r2=randi([1,NP],1,1);
        end
        
        r3=randi([1,NP],1,1);
        while(r3==m)||(r3==r2)||(r3==r1)
            r3=randi([1,NP],1,1);
        end
        %  产生不同的r1,r2,r3
        
        v(m,:)=x(r1,:)+F0*(x(r2,:)-x(r3,:));
 
    end
    
    %   交叉操作
    
    r=randi([1,D],1,1);   % 这个变异是针对整个种群的变异，不正对单个个体
    for n=1:D
        cr=rand;
        if (cr<=CR)||(n==r)
            u(:,n)=v(:,n);
        else
            u(:,n)=x(:,n);
        end
    end
    %     边界条件处理
    for m=1:NP
        for n=1:D
            if u(m,n)<a
                u(m,n)=a;
            end
            if u(m,n)>b
                u(m,n)=b;
            end
        end
    end
    
    % 自然选择
    % 计算新的适应度
    for m=1:NP
        ob_1(m)=sum(u(m,:).^2);
    end
    
    for m=1:NP
        if ob_1(m)<ob(m)
            x(m,:)=u(m,:);
        else
            x(m,:)=x(m,:);
        end
        
    end
    % 现在x为经过选择后的种群
    for m=1:NP
        ob(m)=sum(x(m,:).^2);
    end
    
    trace(gen+1)=min(ob);
    tt=min(ob);
    if gen==210
        break
    end
end
 
x(1,:);
 
figure(1);
title(['差分进化算法(DE)', '最小值: ', num2str(tt)]);
xlabel('迭代次数'); 
ylabel('目标函数值');
plot(trace);