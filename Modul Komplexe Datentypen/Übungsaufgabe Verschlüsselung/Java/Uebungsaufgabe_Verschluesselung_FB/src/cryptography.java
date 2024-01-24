// Florian Böhme 23.01.2024
//TODO write the program so it can accept CLI arguments

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.*;
import java.util.function.Predicate;

import static java.lang.System.exit;

public class cryptography {
    // current working directory is the repo root directory
    private static final String ASSET_PATH = "Modul Komplexe Datentypen\\Übungsaufgabe Verschlüsselung\\Java\\Uebungsaufgabe_Verschluesselung_FB\\assets";
    private static final Predicate<Path> TXT_FILE_FILTER = path -> path.toString().endsWith(".txt");
    private enum STATE_TAGS {ENCRYPT, DECRYPT}
    private static STATE_TAGS currentState;

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
                Do you wish to encrypt or decrypt? (e/u)                
                """);
        System.out.println("#".repeat(60));

        // fetch the input and fetch the files accordingly
        String input = scanner.next();

        Map<String, String> fileContents = null;

        if (input.equalsIgnoreCase("e")) {
            currentState = STATE_TAGS.ENCRYPT;
            fileContents = readTxtFiles(fetchEncryptFiles());
        } else if (input.equalsIgnoreCase("d")) {
            currentState = STATE_TAGS.DECRYPT;
            fileContents = readTxtFiles(fetchDecryptFiles());
        } else {
            System.out.println("#".repeat(60));
            System.out.print("""
                Your input does not match the intended format. Better luck next time!              
                """);
            System.out.println("#".repeat(60));
            exit(666);
        }

        //Talk to user again about the encryption key
        System.out.println("#".repeat(60));
        System.out.print("""
                Great! You have chosen to {{state}}!
                Please insert you encryption key. Currently the service accepts only single integer values
                ranging from 32-255.
                """.replace("{{state}}", String.valueOf(currentState)));
        System.out.println("#".repeat(60));

        // fetch the input from the user
        int cryptKey = 0;
        try {
            cryptKey = Integer.parseInt(scanner.next());
        } catch (NumberFormatException e) {
            System.out.println("You picked the wrong format! Better luck next time!");
            exit(666);
        }

        //negate the key if we want to decrypt for easier traversing over the ascii table
        if (currentState == STATE_TAGS.DECRYPT) {
            cryptKey = -cryptKey;
        }

        // iterate over the files to perform encryption and writeback
        for (Map.Entry<String, String> entry : fileContents.entrySet()) {
            switch (currentState) {
                case ENCRYPT:
                    letsEncrypt(entry.getKey(), entry.getValue(), cryptKey);
                case DECRYPT:
                    letsDecrypt(entry.getValue(), entry.getValue(), cryptKey);
                default:
                    break;
            }
        }

    }

    private static void letsEncrypt(String fileName, String fileContent, int cryptKey) {
        String enctyptedContent = "";
        //TODO Arbeite hier weiter
        for (char character : fileContent.toCharArray()) {
            //sloppy casting and string concatenation but should work
            int rep = (int) character;
            rep = rep + cryptKey;
            enctyptedContent += Character.toChars(rep)[0];
        }
    }

    private static void letsDecrypt(String fileName, String fileContent, int cryptKey) {
    }

    /**
     * Fetches the files inside the asset directory. Filters the file list for file names ending with _encrypted.
     *
     * @return  List<Path>
     * @throws IOException
     */
    private static List<Path> fetchEncryptFiles() throws IOException {
        List<Path> files;

        files = fetchTxtFiles(ASSET_PATH);
        files.removeIf(path -> path.toString().endsWith("_encrypted.txt"));

        return files;
    }

    /**
     * Fetches the files inside the asset directory. Filters the file list for file names ending with _encrypted.
     *
     * @return List<Path>
     * @throws IOException
     */
    private static List<Path> fetchDecryptFiles() throws IOException {
        List<Path> files;

        files = fetchTxtFiles(ASSET_PATH);
        files.removeIf(path -> !path.toString().endsWith("_encrypted.txt"));

        return files;
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
    public static Map<String, String> readTxtFiles(List<Path> txtFiles) throws IOException {
        Map<String, String> contents = new HashMap<>();
        for (Path file : txtFiles) {
            contents.put(file.getFileName().toString(), Files.readString(file));
        }
        return contents;
    }
}
