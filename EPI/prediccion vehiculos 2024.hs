-- Lista de vehículos en circulación Chile, region XIV, de 2020 a 2023.
vehiculos :: [Double]
vehiculos = [113.087, 124.181, 132.709, 140.653]

incremento :: [Double] -> [Double]
incremento xs = zipWith (/) (tail xs) xs  -- divide cada elemento entre el anterior

promedio :: [Double] -> Double
promedio xs = sum xs / fromIntegral(length xs)

main = print $ promedio $ incremento vehiculos 