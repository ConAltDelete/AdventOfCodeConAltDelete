{-# OPTIONS_GHC -Wno-unrecognised-pragmas #-}
{-# HLINT ignore "Use camelCase" #-}
module Main where

import System.IO
import Control.Monad
import Data.Set
import Data.List



main = do
    let list = []
    let ID_compendium = []
    handle <- openFile "input" ReadMode
    content <- hGetContents handle
    let ID_tilde = parse_line contents
    if contain ID_tilde Set("Tolken","<END ID>") then do
        ID_tilde <- combine_id list
    hClose handle

parse_line :: [String] -> Set (String, String)
parse_line [""] = Set("Tolken","<END ID>")
parse_line cont = Set(
    [ break (==':') wc | wc <- word cont]
    )

combine_id :: [Set (String, String)] -> Set(String, String)
combine_id s = s[0] + combine_id s[1..]