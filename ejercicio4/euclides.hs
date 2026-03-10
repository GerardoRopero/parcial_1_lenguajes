import System.CPUTime
import Text.Printf

mcd :: Integer -> Integer -> Integer
mcd a 0 = a
mcd a b = mcd b (a `mod` b)

main = do
    start <- getCPUTime
    let resultado = last [mcd 123456789 987654321 | _ <- [1..10000000]]
    end <- getCPUTime

    let tiempo = fromIntegral (end - start) / (10^12)

    printf "MCD: %d\n" resultado
    printf "Tiempo: %f segundos\n" (tiempo :: Double)
