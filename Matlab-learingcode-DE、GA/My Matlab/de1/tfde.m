function tfde
tic
N = 100; T = 500; pjt=0;

population = -50 + rand(N,5).*100;
pjz=f(population);pjt=pjt+N;
[z,s]=sort(pjz);
population=population(s,:);pjz=z;
Bestfi=[pjz(1)];BestS=[population(1,:)];
t = 1; %代数初始化

while t < T
    
    H_pop = [];
    for i = 1:N
       % add_up = population(i,:) + rand(1,5).*(population(index(1),:)-population(index(2),:));
          %index = sort(fix(rand(1,2).*50)+1);if index(1)==index(2),index(2)= index(2)+1;end
          %   index = sort(fix(rand(1,2).*(N-1)+1));if index(1)==index(2), index(2)=index(1)+1;end
             %add_up = population(fix(N/5*rand)+1,:) + 0.8*rand(1,5).*(population(index(1),:)-population(index(2),:));
           index = sort(fix(rand(1,3).*(N/2-1)+1)); if index(3)==index(2),index(3)=index(3)+5;end;add_up = population(index(1),:) + 0.75*rand(1,5).*(population(index(2),:)-population(index(3),:));
       H_pop = [H_pop; add_up];
    end
 
    V_pop = H_pop;
    for i = 1:N
        for j = 1:5
            if rand < 0.05|V_pop(i,j)<-50|V_pop(i,j)>50 
                V_pop(i,j) = -50+rand*100;
            end
        end
    end
  
   pjzV=f(V_pop);pjt=pjt+N;
  
pjz=[pjz;pjzV];population=[population;V_pop];
[z,s]=sort(pjz);
population=population(s(1:N),:);pjz=z(1:N);
Bestfi=[Bestfi;pjz(1)];BestS=[BestS;population(1,:)];

    t = t + 1;
    if t/10==fix(t/10)
    disp(['当前最优评价：',num2str(Bestfi(end))]) 
    disp(['当前最优解：',num2str(BestS(end,:))]) 
    disp([' '])
    end
    if Bestfi(end)<10E-5,break,end
end
population(1:10,:),
    disp(['当前最优评价：',num2str(Bestfi(end))]) 
    disp(['当前最优解：',num2str(BestS(end,:))]) 

disp(['程序评价次数：',num2str(pjt)])
disp(['程序运行时间：',num2str(toc),'秒！'])
close all ,figure,plot(Bestfi,'*')
end

function y=f(x)
w=size(x,1);
y=sum((x-repmat([1:5],w,1)).^2,2);
end