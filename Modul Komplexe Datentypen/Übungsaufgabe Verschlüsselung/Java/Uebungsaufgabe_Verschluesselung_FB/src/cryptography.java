// Florian Böhme 23.01.2024
//TODO write the program so it can accept CLI arguments

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.function.Predicate;

public class cryptography {
    // current working directory is the repo root directory
    private static final String ASSET_PATH = "Modul Komplexe Datentypen\\Übungsaufgabe Verschlüsselung\\Java\\Uebungsaufgabe_Verschluesselung_FB\\assets";
    private static final Predicate<Path> TXT_FILE_FILTER = path -> path.toString().endsWith(".txt");

    public static void main(String[] args) throws IOException {
        /*String currentDirectory = System.getProperty("user.dir");
        System.out.println("Current working directory: " + currentDirectory);*/

        //First talk to the user via console
        Scanner scanner = new Scanner(System.in);

        System.out.println("#".repeat(60));
        System.out.print("""
                Welcome to your cryptography service. This service is only able to process .txt-Files located in the assets folder.
                It will make a copy of all .txt files inside the assets folder and apply your chosen method to it.
                The program will handle files with their name ending with "_encrypted" as encrypted files. Everything else
                as unencrypted.
                Do you wish to encrypt or unencrypt? (e/u)                
                """);
        System.out.println("#".repeat(60));

        String input = scanner.next();

        if (input.equalsIgnoreCase("e")) {
            letsEncrypt();
        } else if (input.equalsIgnoreCase("u")) {
            letsDecrypt();
        } else {
            System.out.println("#".repeat(60));
            System.out.print("""
                Your input does not match the intended format. Better luck next time!              
                """);
            System.out.println("#".repeat(60));
        }
    }

    /**
     * Fetches the files inside the asset directory. Filters the file list for file names ending with _encrypted.
     * @throws IOException
     */
    private static void letsEncrypt() throws IOException {
        List<Path> files = new ArrayList<>();

        files = fetchTxtFiles(ASSET_PATH);
        files.removeIf(path -> path.toString().endsWith("_encrypted.txt"));

        List<String> fileContents = new ArrayList<>();

        fileContents = readTxtFiles(files);
        //TODO HIer weiter
    }

    /**
     * Fetches the files inside the asset directory. Filters the file list for file names ending with _encrypted.
     * @throws IOException
     */
    private static void letsDecrypt() throws IOException {
        List<Path> files = new ArrayList<>();
        files = fetchTxtFiles(ASSET_PATH);
        files.removeIf(path -> !path.toString().endsWith("_encrypted.txt"));
        readTxtFiles(files);
    }

    /**
     * Returns a list of .txt-files in a given directory path.
     * @param directoryPath
     * @return List<Path>
     * @throws IOException
     */
    public static List<Path> fetchTxtFiles(String directoryPath) throws IOException {

        if (!Files.isDirectory(Paths.get(directoryPath))) {
            throw new IllegalArgumentException("Invalid directory path: " + directoryPath);
        }

        List<Path> files = new ArrayList<>();

        Files.list(Paths.get(directoryPath)).forEach(file -> {
            if (Files.isRegularFile(file) && TXT_FILE_FILTER.test(file)) {
                files.add(file);
            }
        });

        return files;
    }

    /**
     * Returns a list of Strings, each String resembling the contents of one .txt File.
     * @param txtFiles
     * @return List<String>
     * @throws IOException
     */
    public static List<String> readTxtFiles(List<Path> txtFiles) throws IOException {
        List<String> contents = new ArrayList<>();
        for (Path file : txtFiles) {
            contents.addAll(Files.readAllLines(file));
        }
        return contents;
    }
}
