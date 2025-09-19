plot(cmig4)
plot(vamo3)
plot(brfs3)
plot(csna3)
plot(lren3)
# Calcular e plotar a fronteira de portfólio
Basico <- data.frame(na.omit(merge(cmig4, vamo3, brfs3, csna3, lren3, all = FALSE)))

# Renomear as colunas
names(Basico) <- c("cmig4", "vamo3", "brfs3", "csna3", "lren3")
length(lren3) # Para verificar o tamanho
# Transformar em objeto timeSeries para uso com fPortfolio
dados <- timeSeries(Basico)
# Calcular os retornos logarítmicos
Retornos <- returns(dados)

fronteira<-portfolioFrontier(Retornos)
fronteira
frontierPlot(fronteira, auto=F)

# Adicionar pontos específicos ao gráfico (exemplo, pontos que representam portfólios)
# Estes são exemplos fictícios e precisam ser ajustados com base nos seus próprios dados de retorno e risco
points(0.0293,-0.0037 ,pch=19, cex=1.5, col="green")
points(0.0161,-0.0009,pch=19, cex=1.5, col="green")
points(0.0136,0.0019 ,pch=19, cex=1.5, col="green")
points(0.0166,0.0046 ,pch=19, cex=1.5, col="green")
points(0.0237,0.0074,pch=19, cex=1.5, col="red") # Ponto de alto risco


MinimaVariancia<-minvariancePortfolio(Retornos)
PesosMinimos<-getWeights(MinimaVariancia);PesosMinimos
RetornoCalculado<-getTargetReturn(MinimaVariancia);RetornoCalculado
RiscoMinimo<-getTargetRisk(MinimaVariancia);RiscoMinimo
points(0.0136 ,0.0016,pch=19, cex=1.5, col="blue")
GraficoPizza<-weightsPie(MinimaVariancia);GraficoPizza
#--------------------------------------------------------------
CarteiraCustom<-portfolioSpec(portfolio=list(
  weights=NULL,targetReturn=0.003, 
  targetRisk=NULL, riskFreeRate=0.0055131,nFrontierPoints=50))
CarteiraCustom
CarteiraCustomizada<-efficientPortfolio(Retornos, spec=CarteiraCustom)
CarteiraCustomizada
getWeights(CarteiraCustomizada)
getTargetReturn(CarteiraCustomizada)
getTargetRisk(CarteiraCustomizada)
frontierPlot(portfolioFrontier(Retornos))
points(frontierPoints(CarteiraCustomizada)[,1], frontierPoints(CarteiraCustomizada)[,2], col="blue", pch=17, cex=1.5)

singleAssetPoints(fronteira, col="pink", pch=19)
tangencyLines(fronteira, col="green", pch=19)
GraficoPizzaCustom<-weightsPie(CarteiraCustomizada);GraficoPizzaCustom
CarteiraCustom<-portfolioSpec(portfolio=list(
  weights=NULL,targetReturn=0.001, 
  targetRisk=NULL, riskFreeRate=0.0053131,nFrontierPoints=50))
CarteiraCustom
CarteiraCustomizada<-efficientPortfolio(Retornos, spec=CarteiraCustom)
CarteiraCustomizada
getWeights(CarteiraCustomizada)
getTargetReturn(CarteiraCustomizada)
getTargetRisk(CarteiraCustomizada)
frontierPlot(portfolioFrontier(Retornos))
points(frontierPoints(CarteiraCustomizada)[,1], frontierPoints(CarteiraCustomizada)[,2], col="blue", pch=17, cex=1.5)

singleAssetPoints(fronteira, col="pink", pch=19)
tangencyLines(fronteira, col="green", pch=19)
sharpeRatioLines(fronteira, col="red")
tailoredFrontierPlot(portfolioFrontier(Retornos))
GraficoPizzaCustom<-weightsPie(CarteiraCustomizada);
GraficoPizzaCustom
coef(Betacmig4)
coeftest(Betacmig4)
summary(Betacmig4)
coef(Betavamo3)
coeftest(Betavamo3)
summary(Betavamo3)
coef(Betabrfs3)
coeftest(Betabrfs3)
summary(Betabrfs3)
coef(Betacsna3)
coeftest(Betacsna3)
summary(Betacsna3)
coef(Betavamo3)
coeftest(Betavamo3)
summary(Betavamo3)
